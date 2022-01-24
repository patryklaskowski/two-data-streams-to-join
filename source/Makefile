all: build on off

build:
	docker-compose build

on: build
	docker-compose up -d

on_with_logs: on
	docker-compose logs -f -t api

off:
	docker-compose down --remove-orphans
