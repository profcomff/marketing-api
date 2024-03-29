import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from marketing_api.models.base import Base
from marketing_api.models.db import User
from marketing_api.routes.base import app
from marketing_api.settings import get_settings


@pytest.fixture()
def client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope='session')
def dbsession():
    settings = get_settings()
    engine = create_engine(str(settings.DB_DSN))
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()


@pytest.fixture
def user_id(client: TestClient, dbsession: Session):
    res = client.post('v1/user')
    user_id = res.json()['id']
    yield user_id
    db_user = dbsession.query(User).filter(User.id == user_id).one_or_none()
    assert db_user is not None
    dbsession.delete(db_user)
