FROM python:3.11.1-slim AS builder

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

RUN poetry build -f wheel

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
    python3.11 \
    python3-pip \
    libcurl4-openssl-dev \
    ca-certificates \
    && apt-get clean

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1

RUN git clone https://github.com/ggerganov/llama.cpp.git

WORKDIR /app/llama.cpp

RUN LLAMA_CURL=1 make llama-cli

ENV LLAMA_CLI_PATH=/app/llama.cpp/llama-cli

RUN mkdir -p /root/.cache/llama.cpp

WORKDIR /root/.cache/llama.cpp
RUN wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf -O Phi-3-mini-4k-instruct-q4.gguf

WORKDIR /app

# Copy the built wheel from the builder stage
COPY --from=builder /app/dist/*.whl /app
RUN python3 -m pip install --no-cache-dir /app/*.whl

EXPOSE 8000

CMD ["python3", "-m", "transcendai"]
