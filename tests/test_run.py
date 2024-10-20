from src.main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_read_docs():
    response = client.get("/docs")
    assert response.status_code == 200
