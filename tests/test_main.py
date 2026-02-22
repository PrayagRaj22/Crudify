from src import main_route
from fastapi.testclient import TestClient

client = TestClient(main_route)


def test_read_root():
    response = client.get("/")

    assert response.json() == {"message": "Hello World"}
    assert response.status_code == 200
