runserver:
	flask run

createdb:
	flask db init

migrations:
	flask db migrate

migrate:
	flask db upgrade
