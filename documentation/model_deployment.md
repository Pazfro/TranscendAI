Thought process:
- Wasn't sure if i should use the docker image, python lib or compile it myself do I compiled the code and made my own docker image
- My computer almost died. ended up saving cache through th compilation process and my computer was in front of the fan for the whole time


phi3 installation:
- docker pull ollama/ollama
- docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


facebook/nllb installation:
- pip install transformers torch
