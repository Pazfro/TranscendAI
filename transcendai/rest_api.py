# import os
import subprocess

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from transcendai.translation_logics import translate_from_hebrew, translate_to_hebrew

app = FastAPI()


class SummarizeRequest(BaseModel):
    """Request."""

    text: str
    temperature: float = 1.0  # Default is 1.0 for neutral randomness
    max_length: int = 128  # Default maximum length of tokens generated
    top_p: float = 1.0  # Default to 1.0 (no nucleus sampling)
    top_k: int = 50  # Default to 50 for balanced generation
    repetition_penalty: float = 1.0  # Default to no repetition penalty


def send_to_llama(prompt, temperature, max_length, top_p, top_k, repetition_penalty):
    """Send request to module."""
    # llama_cli_path = os.path.join("/root/.cache/llama.cpp", "llama-cli")
    # llama_cli_path = os.path.join(os.path.dirname(__file__), "llama.cpp", "llama-cli")

    # Build the command to call llama-cli with generation parameters
    command = [
        "/home/lior/paz/llama.cpp/llama-cli",
        # llama_cli_path,
        "-m",
        "/home/lior/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf",
        # "-m", "/root/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf",
        "-p",
        f"Please summarize the following text into 5 bullet points: {prompt}",
        "--temp",
        str(temperature),
        "--n_predict",
        str(max_length),
        "--top_p",
        str(top_p),
        "--top_k",
        str(top_k),
        "--repeat_penalty",
        str(repetition_penalty),
    ]
    print(command)

    # Run the llama-cli command as a subprocess
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    # Stream the output back as it becomes available
    def generate_output():
        """Generate stream response."""
        try:
            while True:
                line = process.stdout.readline()
                if not line:  # End of stream
                    break
                translated_line = translate_to_hebrew(line)
                print(translated_line, line)
                yield f"{translated_line}\n"
        except Exception as e:
            yield f"Error: {str(e)}\n"
        finally:
            # Indicate the stream is closed
            yield "\n"

    return generate_output()


@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    """Summarize end point.

    for summarized requests for ai assistant.
    """
    request_text: str = request.text
    if not request_text:
        raise HTTPException(status_code=400, detail="No text provided")
    translated_request = translate_from_hebrew(request_text)
    print(request_text, translated_request)
    return StreamingResponse(
        send_to_llama(
            prompt=translated_request,
            temperature=request.temperature,
            max_length=request.max_length,
            top_p=request.top_p,
            top_k=request.top_k,
            repetition_penalty=request.repetition_penalty,
        ),
        media_type="text/plain",
    )
