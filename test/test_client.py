import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_predict(client):
    response = client.post("/predict", files={"file": "images/test.jpg"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "expected prediction"