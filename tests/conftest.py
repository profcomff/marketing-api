import unittest

from fastapi.testclient import TestClient

from marketing_api.routes.base import app
from marketing_api.routes.models import ActionInfo


class PostTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_can_post_valid_action(self):
        action = ActionInfo(
            user_key="ddd",
            action="INSTALL",
            path_from="http://127.0.0.1:8000/",
            path_to="http://127.0.0.1:8000/me"
        )
        response = self.client.post(f"/action/v1/post", action.json())
        assert response.status_code == 200
