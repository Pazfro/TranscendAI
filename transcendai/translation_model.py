from abc import ABC, abstractmethod

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

from transcendai.logger_config import logger


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

    def __init__(self, model_name: str, src_lang: str, tgt_lang: str) -> None:
        """Initializes the NLLBTranslationModel with the specified model name,
        source language, and target language.

        :param model_name: The model name from Hugging Face.
        :param src_lang: The source language code.
        :param tgt_lang: The target language code.
        """
        self.model_name = model_name
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        logger.info("Loading model: %s", model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
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
        try:
            output = self.translation_pipeline(text)
            translated_text: str = output[0]["translation_text"]
            logger.info("Translated text: %s", translated_text)
            return translated_text
        except Exception as e:
            logger.error("Translation error: %s", str(e))
            raise RuntimeError(f"Error translating: {e}")
