from transcendai.logger_config import logger
from transcendai.translation_model import NLLBTranslationModel

hebrew = "heb_Hebr"
english = "eng_Latn"
model = "facebook/nllb-200-distilled-600M"


def translate_from_hebrew(text: str) -> str:
    """Translating text from hebrew to english."""
    logger.info(f"Translating from hebrew to english: {text}\n")
    translator = NLLBTranslationModel(
        model_name=model, src_lang=hebrew, tgt_lang=english
    )
    translated_text = translator.translate(text)
    return translated_text


def translate_to_hebrew(text: str) -> str:
    """Translating text from hebrew to english."""
    logger.info(f"Translating from english to hebrew: {text}\n")
    translator = NLLBTranslationModel(
        model_name=model, src_lang=english, tgt_lang=hebrew
    )
    translated_text = translator.translate(text)
    return translated_text
