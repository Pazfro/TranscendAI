FROM ubuntu:22.04

WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libstdc++6 \
    python3 \
    python3-pip \
    libcurl4-openssl-dev \
    ca-certificates \
    && apt-get clean

RUN git clone https://github.com/ggerganov/llama.cpp.git

WORKDIR /app/llama.cpp

RUN LLAMA_CURL=1 make llama-cli

RUN mkdir -p /root/.cache/llama.cpp

WORKDIR /root/.cache/llama.cpp
RUN wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf -O Phi-3-mini-4k-instruct-q4.gguf

WORKDIR /app

COPY ../transcendai /app/transcendai

EXPOSE 8000

CMD ["python3", "-m", "transcendai"]
