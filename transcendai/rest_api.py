"""Rest api functionality."""

from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TextPayload(BaseModel):
    """Pydentic payload received from user."""

    text: str


app = FastAPI()


@app.post("/summarize")
async def summarize(payload: TextPayload) -> Dict[str, str]:
    """Summarize end point."""
    text = payload.text

    # Dummy summarization logic
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    summary = text[:100] + "..." if len(text) > 100 else text

    return {"summary": summary}
