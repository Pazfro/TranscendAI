Thought process:
- Wasn't sure if i should use the docker image, python lib or compile it myself do I compiled the code and made my own docker image
- My computer almost died. ended up saving cache through th compilation process and my computer was in front of the fan for the whole time
- In the end i created my own docker :) but for the fast api im using the one created by ollama
- Understood i should use llama.cpp and started from scratch


phi3 installation Local:
- sudo apt install build-essential cmake libcurl4-openssl-dev
- git clone https://github.com/ggerganov/llama.cpp.git
- cd llama.cpp; LLAMA_CURL=1 make clean && LLAMA_CURL=1 make llama-cli
- ./llama-cli --hf-repo "microsoft/Phi-3-mini-4k-instruct-gguf" --hf-file Phi-3-mini-4k-instruct-q4.gguf -p "You are a helpful assistant" --conversation

facebook/nllb installation:
- pip install transformers torch python-bidi(for rtl print)
- Write code that loads the tokenizer and the model (basic_translation.py)
