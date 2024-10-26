FROM ubuntu:24.10

# Install cmake
RUN apt-get update && apt-get install -y cmake wget tar git gcc-13 g++-13
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 10 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-13 10

WORKDIR /app

# Add the NVIDIA CUDA repository and key
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb \
    && dpkg -i cuda-keyring_1.1-1_all.deb \
    && apt-get update \
    && apt-get -y install cuda-toolkit-12-6

# Set environment variables for CUDA
ENV LD_LIBRARY_PATH=/usr/local/cuda/targets/x86_64-linux/lib/stubs:$LD_LIBRARY_PATH
ENV LIBRARY_PATH=/usr/local/cuda/targets/x86_64-linux/lib/stubs:$LIBRARY_PATH
ENV PATH=/usr/local/cuda/bin:$PATH

# Set the Go version
ENV GOLANG_VERSION=1.21.1

# Download and install Go
RUN wget https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go$GOLANG_VERSION.linux-amd64.tar.gz && \
    rm go$GOLANG_VERSION.linux-amd64.tar.gz

# Set Go environment variables
ENV PATH="/usr/local/go/bin:${PATH}"
ENV GOPATH="/go"

# clone ollama repo
RUN git clone https://github.com/ollama/ollama.git

WORKDIR /app/ollama
# Compile ollama
RUN go generate ./...
RUN go build .

RUN cp ollama /bin/ollama

EXPOSE 11434
ENV OLLAMA_HOST=0.0.0.0

ENTRYPOINT ["/bin/ollama"]
CMD ["serve"]

###ollama run llama3.2
