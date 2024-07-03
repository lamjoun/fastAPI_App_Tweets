from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_root() -> None:
    """
    Test the root endpoint.

    Ensures that the root endpoint returns a status code of 200 and the correct
    JSON response.

    Raises:
        AssertionError: If the response does not match the expected values.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World.....!!!!"}


def test_prediction() -> None:
    """
    Test the prediction endpoint.

    Ensures that the prediction endpoint returns a status code of 200 and
    contains a "sentiment" key in the JSON response.

    Raises:
        AssertionError: If the response does not match the expected values.
    """
    response = client.post("/predict", json={"text": "This is a test tweet!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
