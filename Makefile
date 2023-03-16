run:
	source ./venv/bin/activate && uvicorn --reload --log-config logging_dev.conf marketing_api.routes.base:app

configure: venv
	source ./venv/bin/activate && pip install -r requirements.dev.txt -r requirements.txt

venv:
	python3.11 -m venv venv

format:
	source ./venv/bin/activate && autoflake -r --in-place --remove-all-unused-imports ./marketing_api
	source ./venv/bin/activate && isort ./marketing_api
	source ./venv/bin/activate && black ./marketing_api

db:
	docker run -d -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust --name db-marketing-backend postgres:15

migrate:
	source ./venv/bin/activate && alembic upgrade head
