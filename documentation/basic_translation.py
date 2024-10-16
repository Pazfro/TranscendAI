"""Basic use of the facebook/nllb-200-distilled-600m model using the
transformers library."""

from bidi.algorithm import get_display
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

checkpoint = "facebook/nllb-200-distilled-600M"

model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# Sample text to translate
text = "Hello, how are you?"

input_lang = "eng_Latn"
target_lang = "heb_Hebr"
# predictions = model.predict(text, k=1)
# input_lang = predictions[0][0].replace('__label__', '')
translation_pipeline = pipeline(
    "translation",
    model=model,
    tokenizer=tokenizer,
    src_lang=input_lang,
    tgt_lang=target_lang,
    max_length=400,
)
output = translation_pipeline(text)
print(get_display(output[0]["translation_text"]))
