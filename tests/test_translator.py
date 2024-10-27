import pytest
from transformers import M2M100ForConditionalGeneration

from transcendai.translation_model import NLLBTranslationModel


@pytest.fixture(scope="module")
def translator():
    """Fixture for the translator instance."""
    hebrew = "heb_Hebr"
    english = "eng_Latn"
    model_name = "facebook/nllb-200-distilled-600M"
    return NLLBTranslationModel(
        model_name=model_name, src_lang=hebrew, tgt_lang=english
    )


def test_model_loading(translator):
    """Test that model load successfully."""
    assert isinstance(translator.model, M2M100ForConditionalGeneration)


def test_basic_translation(translator):
    """Test a basic translation to ensure functionality."""
    text = "שלום, מה שלומך?"
    result = translator.translate(text)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "how are you?" in result.lower()


def test_short_string_translation(translator):
    """Test the translation of a very short string."""
    text = "אוהל"
    result = translator.translate(text)
    assert isinstance(result, str)
    assert len(result) > 0
    assert result.lower() == "the tent"


def test_long_text_segmentation(translator):
    """Test that segmentation works when input exceeds token limits."""
    text = " ".join(["שם"] * 200)
    result = translator.translate(text)
    assert isinstance(result, str)
    assert len(result) > 0


def test_non_standard_characters(translator):
    """Test translation with non-standard characters or symbols."""
    text = "שלום 😊! מה קורה?"
    result = translator.translate(text)
    assert isinstance(result, str)
    assert len(result) > 0


def test_token_limit_exceeded(translator):
    """Test for when token count exceeds 100 to ensure segmentation occurs."""
    text = " ".join(["Hello, how are you doing today?"] * 20)
    result = translator.translate(text)
    assert isinstance(result, str)
    assert len(result) > 0
