from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_authentication():
    response = client.get("/product/get-all-collection-ids")
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
