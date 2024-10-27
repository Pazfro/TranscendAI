from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "facebook/nllb-200-distilled-600M"

# Download and cache the model and tokenizer
print("Downloading model and tokenizer...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to("cpu").eval()
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

print("Model and tokenizer downloaded successfully.")
