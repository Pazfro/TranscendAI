from pydantic import BaseModel


class SummarizeRequest(BaseModel):
    """Summarize end point request structure."""

    text: str
    translate: bool = True  # Flag to translate Hebrew text to English and also repose
    temperature: float = 1.0  # Default is 1.0 for neutral randomness
    max_length: int = 128  # Default maximum length of tokens generated
    top_p: float = 1.0  # Default to 1.0 (no nucleus sampling)
    top_k: int = 50  # Default to 50 for balanced generation
    repetition_penalty: float = 1.0  # Default to no repetition penalty
