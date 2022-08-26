import time
import unittest
import requests
import uvicorn
from fastapi.testclient import TestClient
from engine.routes.base import app
from multiprocessing import Process
from engine.settings import get_settings
from engine.routes.models import ActionInfo


class PostTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)
        self.url = get_settings().API_URL

    def test_can_post_valid_action(self):
        action = ActionInfo(
            user_key="ddd",
            action="INSTALL",
            path_from="http://127.0.0.1:8000/",
            path_to="http://127.0.0.1:8000/me"
        )
        response = self.client.post(f"{self.url}/action/v1/post", action.json())
        assert response.status_code == 200
