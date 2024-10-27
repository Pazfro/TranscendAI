from fastapi.testclient import TestClient

from transcendai.rest_api import app

client = TestClient(app)


def test_summarize_endpoint():
    """Test endpoint Exists."""
    response = client.post(
        "/summarize",
        json={
            "text": "Summarize this text",
            "translate": False,
            "temperature": 0.8,
            "max_length": 100,
        },
    )
    assert response.status_code == 200


def test_missing_required_parameter():
    """Test Missing required text field."""
    response = client.post("/summarize", json={})
    assert response.status_code == 422


def test_high_temperature():
    """Test high temperature parm."""
    response = client.post(
        "/summarize",
        json={
            "text": "Test high temperature",
            "translate": False,
            "temperature": 0.9,
            "max_length": 50,
        },
    )
    assert response.status_code == 200

    def test_invalid_temperature_parameter():
        """Test invalid param."""
        response = client.post(
            "/summarize",
            json={
                "text": "Some text",
                "translate": False,
                "temperature": -1,
                "max_length": 100,
            },
        )
        assert response.status_code == 422
