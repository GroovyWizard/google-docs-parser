up:
	@echo "Starting container"
	docker-compose up

up-d: 
	@echo "Starting container"
	docker-compose up -d

migrate:
	@echo "Migrating"
	docker exec docsparser bash -c "python manage.py makemigrations"
	docker exec docsparser bash -c "python manage.py migrate"

setup-dev: 
	@echo "Migrating"
	docker exec docsparser bash -c "python manage.py makemigrations"
	docker exec docsparser bash -c "python manage.py migrate"
	docker exec -it docsparser bash -c "python manage.py createsuperuser --email admin@example.com --username admin"

pip:
	docker exec docsparser bash -c "pip install -r requirements.txt"	

sh: 
	docker exec -it docsparser bash

test:
	@echo "Running tests"
	docker exec docsparser bash -c "python manage.py test"