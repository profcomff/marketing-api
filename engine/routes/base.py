import starlette.requests
from ..settings import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from fastapi_sqlalchemy import DBSessionMiddleware
from ..exceptions import DB_Error
from .action import action_router
from fastapi import FastAPI

settings = get_settings()
app = FastAPI()


@app.exception_handler(DB_Error)
def http_DB_error_handler():
    return PlainTextResponse("DB_error",  status_code=500)


app.add_middleware(
    DBSessionMiddleware,
    db_url=settings.DB_DSN,
    session_args={"autocommit": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOW_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

app.include_router(action_router)