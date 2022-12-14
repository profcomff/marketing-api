from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from marketing_api.routes.models import ActionInfo, User
import json


def test_can_post_without_user_id(client: TestClient, dbsession: Session):
    action = dict(
        action="INSTALL",
        path_from="http://127.0.0.1:8000/",
        path_to="http://127.0.0.1:8000/me"
    )
    response = client.post(f"/v1/action", json=action)
    assert response.status_code == 200


def test_can_post_with_user_id(client: TestClient, user_id: int):
    action = dict(
        user_id=user_id,
        action="INSTALL",
        path_from="http://127.0.0.1:8000/",
        path_to="http://127.0.0.1:8000/me"
    )
    response = client.post(f"/v1/action", json=action)
    assert response.status_code == 200


def test_cannot_post_invalid_info(client: TestClient):
    action = {
        "action": "INSTALL",
        "path_to": "http://127.0.0.1:8000/me",
    }
    response = client.post(f"/v1/action", json=action)
    assert response.status_code == 422


def test_can_patch_user(client: TestClient):
    db_user = client.post("/v1/user")
    user_id = db_user.json()['id']
    patch = json.dumps({'union_number': '666'})
    res = client.patch(f"/v1/user/{user_id}", data=patch)
    assert res.json() == {'id': user_id, 'union_number': '666'}


def test_user_create(client: TestClient):
    response = client.post("/v1/user")
    assert response.status_code == 200
