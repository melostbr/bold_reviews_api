runserver:
	flask run

createdb:
	createdb reviews_api

migrations:
	flask db migrate

migrate:
	flask db upgrade
