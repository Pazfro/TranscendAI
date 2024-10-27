import pytest
from pydantic import ValidationError

from transcendai.schemas import SummarizeRequest


def test_valid_summarize_request():
    """Test valid summarize request."""
    request = SummarizeRequest(
        text="Summarize this",
        temperature=0.7,
        max_length=150,
        top_p=0.9,
        top_k=50,
        repeat_penalty=1.1,
    )
    assert request.text == "Summarize this"
    assert request.temperature == 0.7
    assert request.max_length == 150


def test_missing_required_field():
    """Test missing required field."""
    with pytest.raises(ValidationError):
        SummarizeRequest()


def test_boundary_values():
    """Test the boundaries of the values."""
    request = SummarizeRequest(
        text="Boundary test",
        temperature=0.0,
        max_length=1,
        top_p=0.0,
        top_k=1,
        repetition_penalty=1.0,
    )
    assert request.temperature == 0.0
    assert request.max_length == 1
    assert request.top_p == 0.0
    assert request.top_k == 1
    assert request.repetition_penalty == 1.0
