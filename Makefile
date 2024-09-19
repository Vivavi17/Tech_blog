app_port = 8080
export PYTHONPATH = $(shell echo $PYTHONPATH):$(shell pwd)

start:
	docker compose build
	docker compose up

run_app:
	python3 src/main.py

run_dockerfile:
	docker run -p ${app_port}:${app_port} --env-file .env 'tech_blog_app'

build: env_file
	docker build --tag 'tech_blog_app' .

env_file:
ifeq (,$(wildcard .env))
	@echo "Creating .env file from .env-example..."
	cp .env-example .env
endif

clean:
	docker stop $(shell docker ps -q --filter ancestor=tech_blog_app ) 2>/dev/null || true
	docker rm $(shell docker ps -a -q --filter "ancestor=tech_blog_app") 2>/dev/null || true

clean_volumes:
	docker volume ls -q | xargs docker volume rm

rebuild: clean build