from transcendai.translation_model import NLLBTranslationModel

hebrew = "heb_Hebr"
english = "eng_Latn"
checkpoint = "facebook/nllb-200-distilled-600M"


def translate_from_hebrew(text: str) -> str:
    """Translating text from hebrew to english."""
    print(f"translate to english: {text}\n\n")
    translator = NLLBTranslationModel(
        model_name=checkpoint, src_lang=hebrew, tgt_lang=english
    )
    translated_text = translator.translate(text)
    return translated_text


def translate_to_hebrew(text: str) -> str:
    """Translating text from hebrew to english."""
    print(f"translaten to hebrew: {text}\n\n")
    translator = NLLBTranslationModel(
        model_name=checkpoint, src_lang=english, tgt_lang=hebrew
    )
    translated_text = translator.translate(text)
    return translated_text
