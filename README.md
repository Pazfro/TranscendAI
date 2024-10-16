# TranscendAI
A REST API application featuring a machine learning model designed for flexible input handling, integrated with a language model for real-time translation between languages. The system efficiently processes user queries, delivering accurate responses while providing seamless translation between the supported languages.

## USE
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"text": "This is a sample text that will be used to demonstrate the summarization feature of this FastAPI endpoint."}'
```

curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"text": "שלום מה קורה"}'
```
