name = fbotics
registry = aibotics
user_id = $(shell id -u $(USER))


.PHONY: build
# target: build – build the docker image
build:
	docker-compose -f docker-compose.yml build

.PHONY: up
# target: up – setup the whole system with requirements
up: down
	LOCAL_USER_ID=$(user_id) docker-compose -f docker-compose.yml up

.PHONY: run
# target: run – go inside the container
run:
	LOCAL_USER_ID=$(user_id) docker exec -it fbotics_fbotics_1 bash

.PHONY: down
# target: down – stops and remoces containers
down:
	LOCAL_USER_ID=$(user_id) docker-compose -f docker-compose.yml down -v

.PHONY: test
# target: test – execute the tests
test:
	LOCAL_USER_ID=$(USER_ID) docker-compose run fbotics python -m pytest -vv fbotics/tests/functional

.PHONY: upload
# target: upload – upload the package to Python package index
upload:
	LOCAL_USER_ID=$(USER_ID) docker-compose run fbotics python setup.py sdist bdist_wheel & twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: doc
# target: doc – generate documentation and start local server
doc:
	LOCAL_USER_ID=$(USER_ID) docker-compose run -p 8082:8000 -w /usr/src/app/docs fbotics bash -c "python autogen.py & sleep 5 & mkdocs serve -f /usr/src/app/docs/mkdocs.yml"

.PHONY: upload_doc
# target: upload_doc – upload the documentation to GitHub Pages
upload_doc:
	LOCAL_USER_ID=$(USER_ID) docker-compose run fbotics mkdocs gh-deploy -f docs/mkdocs.yml

.PHONY: clean
# target: clean – clean the project's directory
clean:
	@find . \
		-name *.py[cod] -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +
	rm -rf build/
	rm -rf dist/
	rm -rf fbotics.egg-info

.PHONY: help
# target: help – display all callable targets
help:
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| sed -r "s/^\s*#\s*target\s*:\s*//g"
	@echo
