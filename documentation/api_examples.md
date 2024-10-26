1. Deterministic, Focused Output (Low temperature):
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizaa?", "temperature": 0.2, "max_length": 50, "top_p": 0.9}'
```
Expected Output: The summary will be short and focused, with minimal randomness and creativity.

2. Creative and Diverse Output (High temperature):
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizaa?", "temperature": 1.8, "max_length": 100, "top_p": 1.0}'
```
Expected Output: The summary will be more creative, possibly less predictable, and may include more diverse phrasing.

3. Short Output with Max Token Limit (max_length):
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizaa?", "max_length": 20}'
```
Expected Output: The output will be limited to just 20 tokens, so it will be concise.

4. Nucleus Sampling with Top p Value:
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizaa?", "top_p": 0.7}'
```
Expected Output: The model will select tokens from the top 70% of the most probable options, leading to more diverse output without going too far off track.

5. Controlled Repetition:
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizza?", "repetition_penalty": 1.2}'
```
Expected Output: The model will avoid repeating the same phrases, creating a more varied response.

6. Deterministic Output with Low top_k:
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizza?", "top_k": 5}'
```
Expected Output: The output will be more deterministic and focused, as the model will only consider the top 5 most likely tokens at each step.

7. Diverse Output with High top_k and Controlled Repetition:
```bash
curl -X POST http://localhost:8000/summarize \
  -H "Content-Type: application/json" \
  -d '{"text": "How to make pizza?", "top_k": 100, "repetition_penalty": 1.5}'
```
Expected Output: The output will be more diverse with less repetition, as the model will consider a wider range of tokens (top 100) and penalize repetitive phrases.
