from fastapi.testclient import TestClient

from fastemplate import app

client_app = TestClient(app)
