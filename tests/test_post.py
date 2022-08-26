from fastapi.testclient import TestClient

from marketing_api.routes.base import app
from marketing_api.routes.models import ActionInfo


def test_post():
    client = TestClient(app)
    action = ActionInfo(
        user_id=1,
        action="INSTALL",
        path_from="http://127.0.0.1:8000/",
        path_to="http://127.0.0.1:8000/me"
    )
    response = client.post(f"/v1/action", action.json())
    assert response.status_code == 204


def test_user_create():
    client = TestClient(app)
    response = client.post("/v1/user")
    assert response.status_code == 200

