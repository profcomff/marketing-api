from fastapi.testclient import TestClient

from marketing_api.routes.base import app
from marketing_api.routes.models import ActionInfo, User


def test_can_post_without_user_id():
    client = TestClient(app)
    action = ActionInfo(
        action="INSTALL",
        path_from="http://127.0.0.1:8000/",
        path_to="http://127.0.0.1:8000/me"
    )
    response = client.post(f"/v1/action", action.json())
    assert response.status_code == 204


def test_can_post_with_user_id():
    client = TestClient(app)
    action = ActionInfo(
        user_id=1,
        action="INSTALL",
        path_from="http://127.0.0.1:8000/",
        path_to="http://127.0.0.1:8000/me"
    )
    response = client.post(f"/v1/action", action.json())
    assert response.status_code == 204


def test_cannot_post_invalid_info():
    client = TestClient(app)
    action = {
        "action":"INSTALL",
        "path_to":"http://127.0.0.1:8000/me",
    }
    response = client.post(f"/v1/action", json=action)
    assert response.status_code == 422


def test_can_patch_user():
    client = TestClient(app)
    db_user = client.post("/v1/user")
    user = User(**db_user.json())
    client.patch(f"/v1/user/{user.id}?union_number={406}")


def test_user_create():
    client = TestClient(app)
    response = client.post("/v1/user")
    assert response.status_code == 200


if __name__ == "__main__":
    test_can_patch_user()