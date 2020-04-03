# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import inspect
import os
import re
import shutil
import sys

import fbotics
from fbotics.client import Client

if sys.version[0] == "2":
    reload(sys)
    sys.setdefaultencoding("utf8")

EXCLUDE = {}

PAGES = [
    {
        "page": "receipt_template/receipt_template.md",
        "classes": [
            fbotics.models.payloads.receipt_template.ReceiptTemplatePayload,
            fbotics.models.payloads.receipt_template.Element,
            fbotics.models.payloads.receipt_template.Address,
            fbotics.models.payloads.receipt_template.Summary,
            fbotics.models.payloads.receipt_template.Adjustment,
        ],
    },
    {
        "page": "list_template/list_template.md",
        "classes": [fbotics.models.payloads.list_template.ListTemplatePayload],
    },
    {
        "page": "generic_template/generic_template.md",
        "classes": [fbotics.models.payloads.generic_template.GenericTemplatePayload],
    },
    {
        "page": "client/client.md",
        "methods": [
            Client.send_button_template,
            Client.send_text,
            Client.send_audio,
            Client.send_image,
            Client.send_file,
            Client.send_generic_template,
            Client.send_quick_replies,
        ],
    },
    {
        "page": "quick_replies/quick_replies.md",
        "classes": [fbotics.models.quick_reply.QuickReply],
    },
    {
        "page": "buttons/buttons.md",
        "classes": [
            fbotics.models.buttons.WebUrlButton,
            fbotics.models.buttons.CallButton,
            fbotics.models.buttons.PostbackButton,
        ],
    },
]

ROOT = "http://fbotics.io/"


def get_class_attr(Cls) -> []:
    import re

    return [
        a
        for a, v in Cls.__dict__.items()
        if not re.match("<function.*?>", str(v))
        and not (a.startswith("__") and a.endswith("__"))
    ]


def get_class_attr_val(cls):
    attr = get_class_attr(type(cls))
    attr_dict = {}
    for a in attr:
        attr_dict[a] = getattr(cls, a)
    return attr_dict


def get_function_signature(function, method=True):
    wrapped = getattr(function, "_original_function", None)

    if wrapped is None:
        signature = inspect.getargspec(function)
    else:
        signature = inspect.getargspec(wrapped)
    defaults = signature.defaults
    if method:
        args = signature.args[1:]
    else:
        args = signature.args
    if defaults:
        kwargs = zip(args[-len(defaults) :], defaults)
        args = args[: -len(defaults)]
    else:
        kwargs = []
    st = "%s.%s(" % (function.__module__, function.__name__)

    for a in args:
        st += str(a) + ", "
    for a, v in kwargs:
        if isinstance(v, str):
            v = "'" + v + "'"
        st += str(a) + "=" + str(v) + ", "
    if kwargs or args:
        signature = st[:-2] + ")"
    else:
        signature = st + ")"
    return signature


def get_class_signature(cls):
    signature = "%s.%s(" % (cls.__module__, cls.__name__)
    class_attr_value_dict = get_class_attr_val(cls())
    class_attr_value_dict.pop("_schema")
    for k, v in class_attr_value_dict.items():
        signature += str(k) + "=" + str(v) + ", "
    signature = signature[:-2] + ")"
    return signature


def class_to_docs_link(cls):
    module_name = cls.__module__
    module_name = module_name[6:]
    link = ROOT + module_name.replace(".", "/") + "#" + cls.__name__.lower()
    return link


def class_to_source_link(cls):
    module_name = cls.__module__
    path = module_name.replace(".", "/")
    path += ".py"
    line = inspect.getsourcelines(cls)[-1]
    link = "https://github.com/pasmod/" "fbotics/blob/master/" + path + "#L" + str(line)
    return "[[source]](" + link + ")"


def code_snippet(snippet):
    result = "```python\n"
    result += snippet + "\n"
    result += "```\n"
    return result


def count_leading_spaces(s):
    ws = re.search(r"\S", s)
    if ws:
        return ws.start()
    else:
        return 0


def process_list_block(docstring, starting_point, section_end, leading_spaces, marker):
    ending_point = docstring.find("\n\n", starting_point)
    block = docstring[
        starting_point : (None if ending_point == -1 else ending_point - 1)
    ]
    # Place marker for later reinjection.
    docstring_slice = docstring[starting_point:section_end].replace(block, marker)
    docstring = docstring[:starting_point] + docstring_slice + docstring[section_end:]
    lines = block.split("\n")
    # Remove the computed number of leading white spaces from each line.
    lines = [re.sub("^" + " " * leading_spaces, "", line) for line in lines]
    # Usually lines have at least 4 additional leading spaces.
    # These have to be removed, but first the list roots have to be detected.
    top_level_regex = r"^    ([^\s\\\(]+):(.*)"
    top_level_replacement = r"- __\1__:\2"
    lines = [re.sub(top_level_regex, top_level_replacement, line) for line in lines]
    # All the other lines get simply the 4 leading space (if present) removed
    lines = [re.sub(r"^    ", "", line) for line in lines]
    # Fix text lines after lists
    indent = 0
    text_block = False
    for i in range(len(lines)):
        line = lines[i]
        spaces = re.search(r"\S", line)
        if spaces:
            # If it is a list element
            if line[spaces.start()] == "-":
                indent = spaces.start() + 1
                if text_block:
                    text_block = False
                    lines[i] = "\n" + line
            elif spaces.start() < indent:
                text_block = True
                indent = spaces.start()
                lines[i] = "\n" + line
        else:
            text_block = False
            indent = 0
    block = "\n".join(lines)
    return docstring, block


def process_docstring(docstring):
    # First, extract code blocks and process them.
    code_blocks = []
    if "```" in docstring:
        tmp = docstring[:]
        while "```" in tmp:
            tmp = tmp[tmp.find("```") :]
            index = tmp[3:].find("```") + 6
            snippet = tmp[:index]
            # Place marker in docstring for later reinjection.
            docstring = docstring.replace(snippet, "$CODE_BLOCK_%d" % len(code_blocks))
            snippet_lines = snippet.split("\n")
            # Remove leading spaces.
            num_leading_spaces = snippet_lines[-1].find("`")
            snippet_lines = [snippet_lines[0]] + [
                line[num_leading_spaces:] for line in snippet_lines[1:]
            ]
            # Most code snippets have 3 or 4 more leading spaces
            # on inner lines, but not all. Remove them.
            inner_lines = snippet_lines[1:-1]
            leading_spaces = None
            for line in inner_lines:
                if not line or line[0] == "\n":
                    continue
                spaces = count_leading_spaces(line)
                if leading_spaces is None:
                    leading_spaces = spaces
                if spaces < leading_spaces:
                    leading_spaces = spaces
            if leading_spaces:
                snippet_lines = (
                    [snippet_lines[0]]
                    + [line[leading_spaces:] for line in snippet_lines[1:-1]]
                    + [snippet_lines[-1]]
                )
            snippet = "\n".join(snippet_lines)
            code_blocks.append(snippet)
            tmp = tmp[index:]

    # Format docstring lists.
    section_regex = r"\n( +)# (.*)\n"
    section_idx = re.search(section_regex, docstring)
    shift = 0
    sections = {}
    while section_idx and section_idx.group(2):
        anchor = section_idx.group(2)
        leading_spaces = len(section_idx.group(1))
        shift += section_idx.end()
        next_section_idx = re.search(section_regex, docstring[shift:])
        if next_section_idx is None:
            section_end = -1
        else:
            section_end = shift + next_section_idx.start()
        marker = "$" + anchor.replace(" ", "_") + "$"
        docstring, content = process_list_block(
            docstring, shift, section_end, leading_spaces, marker
        )
        sections[marker] = content
        # `docstring` has changed, so we can't use `next_section_idx` anymore
        # we have to recompute it
        section_idx = re.search(section_regex, docstring[shift:])

    # Format docstring section titles.
    docstring = re.sub(r"\n(\s+)# (.*)\n", r"\n\1__\2__\n\n", docstring)

    # Strip all remaining leading spaces.
    lines = docstring.split("\n")
    docstring = "\n".join([line.lstrip(" ") for line in lines])

    # Reinject list blocks.
    for marker, content in sections.items():
        docstring = docstring.replace(marker, content)

    # Reinject code blocks.
    for i, code_block in enumerate(code_blocks):
        docstring = docstring.replace("$CODE_BLOCK_%d" % i, code_block)
    return docstring


template_np_implementation = """# Numpy implementation

    ```python
{{code}}
    ```
"""

template_hidden_np_implementation = """# Numpy implementation

    <details>
    <summary>Show the Numpy implementation</summary>

    ```python
{{code}}
    ```

    </details>
"""


def add_np_implementation(function, docstring):
    np_implementation = getattr(numpy_backend, function.__name__)
    code = inspect.getsource(np_implementation)
    code_lines = code.split("\n")
    for i in range(len(code_lines)):
        if code_lines[i]:
            # if there is something on the line, add 8 spaces.
            code_lines[i] = "        " + code_lines[i]
    code = "\n".join(code_lines[:-1])

    if len(code_lines) < 10:
        section = template_np_implementation.replace("{{code}}", code)
    else:
        section = template_hidden_np_implementation.replace("{{code}}", code)
    return docstring.replace("{{np_implementation}}", section)


print("Cleaning up existing sources directory.")
if os.path.exists("sources"):
    shutil.rmtree("sources")

print("Populating sources directory with templates.")
for subdir, dirs, fnames in os.walk("templates"):
    for fname in fnames:
        new_subdir = subdir.replace("templates", "sources")
        if not os.path.exists(new_subdir):
            os.makedirs(new_subdir)
        if fname[-3:] == ".md":
            fpath = os.path.join(subdir, fname)
            new_fpath = fpath.replace("templates", "sources")
            shutil.copy(fpath, new_fpath)


def read_file(path):
    with open(path) as f:
        return f.read()


def collect_class_methods(cls, methods):
    if isinstance(methods, (list, tuple)):
        return [getattr(cls, m) if isinstance(m, str) else m for m in methods]
    methods = []
    for _, method in inspect.getmembers(cls, predicate=inspect.isroutine):
        if method.__name__[0] == "_" or method.__name__ in EXCLUDE:
            continue
        methods.append(method)
    return methods


def render_function(function, method=True):
    subblocks = []
    signature = get_function_signature(function, method=method)
    if method:
        signature = signature.replace(function.__module__ + ".", "")
    subblocks.append("### " + function.__name__ + "\n")
    subblocks.append(code_snippet(signature))
    docstring = function.__doc__
    if docstring:
        if "backend" in signature and "{{np_implementation}}" in docstring:
            docstring = add_np_implementation(function, docstring)
        subblocks.append(process_docstring(docstring))
    return "\n\n".join(subblocks)


def read_page_data(page_data, type):
    assert type in ["classes", "functions", "methods"]
    data = page_data.get(type, [])
    for module in page_data.get("all_module_{}".format(type), []):
        module_data = []
        for name in dir(module):
            if name[0] == "_" or name in EXCLUDE:
                continue
            module_member = getattr(module, name)
            if (
                inspect.isclass(module_member)
                and type == "classes"
                or inspect.isfunction(module_member)
                and type == "functions"
            ):
                instance = module_member
                if module.__name__ in instance.__module__:
                    if instance not in module_data:
                        module_data.append(instance)
        module_data.sort(key=lambda x: id(x))
        data += module_data
    return data


if __name__ == "__main__":
    readme = read_file("../README.md")
    index = read_file("templates/index.md")
    index = index.replace("{{autogenerated}}", readme[readme.find("##") :])
    with open("sources/index.md", "w") as f:
        f.write(index)

    # TODO: get the version of the fbotics package
    print("Generating docs for FBotics %s." % "1.0.0")
    for page_data in PAGES:
        classes = read_page_data(page_data, "classes")

        blocks = []
        for element in classes:
            if not isinstance(element, (list, tuple)):
                element = (element, [])
            cls = element[0]
            subblocks = []
            signature = get_class_signature(cls)
            subblocks.append(
                '<span style="float:right;">' + class_to_source_link(cls) + "</span>"
            )
            if element[1]:
                subblocks.append("## " + cls.__name__ + " class\n")
            else:
                subblocks.append("### " + cls.__name__ + "\n")
            subblocks.append(code_snippet(signature))
            docstring = cls.__doc__
            if docstring:
                subblocks.append(process_docstring(docstring))
            methods = collect_class_methods(cls, element[1])
            if methods:
                subblocks.append("\n---")
                subblocks.append("## " + cls.__name__ + " methods\n")
                subblocks.append(
                    "\n---\n".join(
                        [render_function(method, method=True) for method in methods]
                    )
                )
            blocks.append("\n".join(subblocks))

        methods = read_page_data(page_data, "methods")

        for method in methods:
            blocks.append(render_function(method, method=True))

        functions = read_page_data(page_data, "functions")

        for function in functions:
            blocks.append(render_function(function, method=False))

        if not blocks:
            raise RuntimeError("Found no content for page " + page_data["page"])

        mkdown = "\n----\n\n".join(blocks)
        # save module page.
        # Either insert content into existing page,
        # or create page otherwise
        page_name = page_data["page"]
        path = os.path.join("sources", page_name)
        if os.path.exists(path):
            template = read_file(path)
            assert "{{autogenerated}}" in template, (
                "Template found for " + path + " but missing {{autogenerated}}" " tag."
            )
            mkdown = template.replace("{{autogenerated}}", mkdown)
            print("...inserting autogenerated content into template:", path)
        else:
            print("...creating new page with autogenerated content:", path)
        subdir = os.path.dirname(path)
        if not os.path.exists(subdir):
            os.makedirs(subdir)
        with open(path, "w") as f:
            f.write(mkdown)
