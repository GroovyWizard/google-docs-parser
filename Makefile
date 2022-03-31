up:
	@echo "Starting container"
	docker-compose up

up-d: 
	@echo "Starting container"
	docker-compose up -d 

setup:
	@echo "Migrating"
	docker exec docsparser bash -c "python manage.py makemigrations"
	docker exec docsparser bash -c "python manage.py migrate"
pip:
	docker exec -it docsparser bash -c "pip install -r requirements.txt"	