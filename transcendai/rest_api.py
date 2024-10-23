import subprocess

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from transcendai.translation_logics import translate

app = FastAPI()


class SummarizeRequest(BaseModel):
    """Summarizze Request."""

    text: str


llama_process = None


def llama_model(prompt):
    """Request from model with llama.cpp."""
    global llama_process
    # llama_cli_path = os.path.join(os.path.dirname(__file__), "llama.cpp", "llama-cli")

    command = [
        "/home/lior/paz/llama.cpp/llama-cli",
        # llama_cli_path,
        "-m",
        "/home/lior/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf",
        # "-m", "/root/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf",
        "-p",
        f"Please summarize the following text into 5 bullet points: f'{prompt}'",
    ]

    llama_process = subprocess.Popen(
        command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    def generate_output():
        """Streams the out put."""
        try:
            while True:
                line = llama_process.stdout.readline()
                if not line:  # End of stream
                    break
                yield line
        except Exception as e:
            yield f"Error: {str(e)}\n"
        finally:
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
    translated_request = translate(request_text)
    print(request_text, request)
    return StreamingResponse(llama_model(translated_request), media_type="text/plain")
