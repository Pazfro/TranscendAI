#!/usr/bin/env bash

#phi3 installation
sudo apt install build-essential cmake libcurl4-openssl-dev git
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp || exit
LLAMA_CURL=1 make clean && LLAMA_CURL=1 make llama-cli
./llama-cli --hf-repo "microsoft/Phi-3-mini-4k-instruct-gguf" --hf-file Phi-3-mini-4k-instruct-q4.gguf -p "You are a helpful assistant" --conversation

#transformers installation for nllb model
python3 -m pip install transformers torch python-bidi
