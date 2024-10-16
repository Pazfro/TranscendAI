from transcendai.translation_model import NLLBTranslationModel

input_lang = "heb_Hebr"
target_lang = "eng_Latn"


def translate(text: str) -> str:
    """Translating text from hebrew to english."""
    translator = NLLBTranslationModel(input_lang, target_lang)
    translated_text = translator.translate(text)
    return translated_text
