import pytest
from fastapi.testclient import TestClient
from src.routes import user_routes
from src.routes.items import items

client = TestClient(user_routes)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    items.clear()
    yield
