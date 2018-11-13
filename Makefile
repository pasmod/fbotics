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

.PHONY: clean
# target: clean – clean the project's directory
clean:
	@find . \
		-name *.py[cod] -exec rm -fv {} + -o \
		-name __pycache__ -exec rm -rfv {} +

.PHONY: help
# target: help – display all callable targets
help:
	@echo
	@egrep "^\s*#\s*target\s*:\s*" [Mm]akefile \
	| sed -r "s/^\s*#\s*target\s*:\s*//g"
	@echo
