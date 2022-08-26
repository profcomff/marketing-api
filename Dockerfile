FROM python:3.10
WORKDIR /app

COPY ./requirements.txt /app/
COPY ./gunicorn_conf.py /app/gunicorn_conf.py
COPY engine /app/engine

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-c", "/app/gunicorn_conf.py", "engine.routes.base:app" ]
