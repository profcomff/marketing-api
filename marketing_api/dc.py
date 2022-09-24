from sqlalchemy import create_engine
from settings import get_settings
from models.base import Base


engine = create_engine(get_settings().DB_DSN)


def drop():
    Base.metadata.drop_all(engine)


def create():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create()
