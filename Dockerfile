FROM python:3.10
WORKDIR /app

COPY ./requirements.txt /app/
COPY ./gunicorn_conf.py /app/gunicorn_conf.py
COPY marketing_api /app/marketing_api

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn_conf.py", "marketing_api.routes.base:app" ]
