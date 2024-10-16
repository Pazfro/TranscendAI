from abc import ABC, abstractmethod

from bidi.algorithm import get_display
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


class TranslationModel(ABC):
    """Abstract base class for translation models."""

    @abstractmethod
    def translate(self, text: str) -> str:
        """Translates the given text to the target language.

        :param text: The text to be translated.
        :return: The translated text.
        """
        pass


class NLLBTranslationModel(TranslationModel):
    """Class for handling translations using the NLLB-200 model from Hugging
    Face."""

    CHECKPOINT = "facebook/nllb-200-distilled-600M"

    def __init__(self, src_lang: str, tgt_lang: str) -> None:
        """Initializes the NLLBTranslationModel with the specified model name,
        source language, and target language.

        :param src_lang: The source language code.
        :param tgt_lang: The target language code.
        """
        self.model_name = NLLBTranslationModel.CHECKPOINT
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.translation_pipeline = pipeline(
            "translation",
            model=self.model,
            tokenizer=self.tokenizer,
            src_lang=self.src_lang,
            tgt_lang=self.tgt_lang,
            max_length=400,
        )

    def translate(self, text: str) -> str:
        """Translates the given text to the target language.

        :param text: The text to be translated.
        :return: The translated text in the target language.
        """
        output = self.translation_pipeline(text)
        return get_display(output[0]["translation_text"])
