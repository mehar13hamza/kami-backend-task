
.PHONY: build
build: ## Build developer containers.
	docker compose build


.PHONY: up
up: ## Build developer containers.
	docker compose up


.PHONY: down
down: ## Build developer containers.
	docker compose down


.PHONY: silenceup
silenceup: ## Build developer containers.
	docker compose up -d

.PHONY: tests
tests: ## Build developer containers.
	docker compose run --rm web python manage.py test

.PHONY: makemigrations
makemigrations: ## Build developer containers.
	docker compose run --rm web python manage.py makemigrations


.PHONY: migrate
migrate: ## Build developer containers.
	docker compose run --rm web python manage.py migrate

.PHONY: coverage-report
coverage-report:
	docker-compose run --rm web coverage run manage.py test;
	docker-compose run --rm web coverage report  

.PHONY: coverage-report-in-html
coverage-report-in-html:
	docker-compose run --rm web coverage run manage.py test;
	docker-compose run --rm web coverage html 

#add .dockerignore
#make migration command
# remove migrates and add makemigration
#mount db volume in docker compose
#add in read me clone instructions and what to replace in env