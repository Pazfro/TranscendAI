from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse

from transcendai.logger_config import logger
from transcendai.phi3_instruct_model import LlamaHandler
from transcendai.schemas import SummarizeRequest
from transcendai.translation_logics import translate_from_hebrew

app = FastAPI()
llama_handler = LlamaHandler(
    model_path="/root/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf"
)


@app.post("/summarize")
async def summarize(request: SummarizeRequest) -> StreamingResponse:
    """Summarize end point.

    Summarizing client requests in hebrew and in english.
    """
    input_request: str = request.text
    if not input_request:
        logger.warning("No request provided in request.")
        raise HTTPException(status_code=400, detail="No text provided")

    logger.info(f"Summarize request {input_request}")

    if request.translate:
        try:
            input_request = translate_from_hebrew(input_request)
            logger.info("Translated summarize request.")
        except Exception as e:
            logger.error(f"Translation error: {e}")
            raise HTTPException(status_code=500, detail="Error during translation")

    request.text = input_request
    logger.info(f"Processing request: text length {input_request} characters")

    # Stream the response from LLaMA handler
    return StreamingResponse(
        llama_handler.process_text(request), media_type="text/plain"
    )
