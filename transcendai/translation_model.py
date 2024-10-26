from abc import ABC, abstractmethod

import nltk
from nltk import sent_tokenize
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

from transcendai.logger_config import logger

nltk.download("punkt_tab")


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
    Face.

    Optimized for CPU with segmentation and fast tokenization.
    """

    TENSOR_SEQUENCE_LENGTH_INDEX = 1

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

        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cpu").eval()
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

        self.translation_pipeline = pipeline(
            "translation",
            model=self.model,
            tokenizer=self.tokenizer,
            src_lang=self.src_lang,
            tgt_lang=self.tgt_lang,
            max_length=100,  # Limit for efficient processing
        )

    def translate(self, text: str) -> str:
        """Translates text with segmentation if it exceeds 100 tokens. Text is
        split into sentences if necessary, translated individually, and
        reassembled.

        :param text: The text to be translated.
        :return: The translated text in the target language.
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=False)
        if (
            inputs.input_ids.shape[NLLBTranslationModel.TENSOR_SEQUENCE_LENGTH_INDEX]
            <= 100
        ):
            try:
                translated_text = self._translate_single_segment(text)
            except Exception as e:
                logger.error("Error Translating text: %s", str(e))
                raise RuntimeError("Error Translating text")
            return translated_text
        else:
            logger.info("Text exceeds 100 tokens, segmenting for translation.")
            try:
                sentences = sent_tokenize(text)
                translated_sentences = [
                    self._translate_single_segment(sentence) for sentence in sentences
                ]
                translated_text = " ".join(translated_sentences)
            except Exception as e:
                logger.error("Error Translating text: %s", str(e))
                raise RuntimeError("Error Translating text")
            return translated_text

    def _translate_single_segment(self, segment: str) -> str:
        """Translates a single text segment that is within the token limit.

        :param segment: A single text segment to be translated.
        :return: Translated text for the segment.
        """
        try:
            output = self.translation_pipeline(segment)
            translated_text = output[0]["translation_text"]
            logger.info("Translated segment: %s", translated_text)
            return translated_text
        except Exception as e:
            logger.error("Error single segment translation: %s", str(e))
            raise RuntimeError("Error single segment translation")
