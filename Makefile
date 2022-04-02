up:
	@echo "Starting container"
	docker-compose up -d

down: 
	@echo "Stopping container"
	docker-compose down

up-int: 
	@echo "Starting container"
	docker-compose up 

build:
	@echo "Building container"
	docker-compose build

migrate:
	@echo "Migrating"
	docker exec -it docsparser bash -c "python manage.py makemigrations"
	docker exec docsparser bash -c "python manage.py migrate"

setup-dev: 
	@echo "Migrating"
	docker exec docsparser bash -c "python manage.py makemigrations"
	docker exec docsparser bash -c "python manage.py migrate"
	docker exec -it docsparser bash -c "python manage.py createsuperuser --email admin@example.com --username admin"

pip:
	docker exec docsparser bash -c "pip3 install -r requirements.txt"	

sh: 
	docker exec -it docsparser bash

test:
	@echo "Running tests"
	docker exec docsparser bash -c "python manage.py test"