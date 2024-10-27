from pydantic import BaseModel, Field
from typing_extensions import Annotated


class SummarizeRequest(BaseModel):
    """Summarize end point request structure."""

    text: Annotated[
        str,
        Field(
            min_length=1, max_length=4000, description="Input text for summarization."
        ),
    ]
    translate: Annotated[
        bool,
        Field(
            default=True,
            description="Flag to translate Hebrew text to English and also repose.",
        ),
    ]
    temperature: Annotated[
        float,
        Field(
            default=1.0,
            ge=0.0,
            le=1.0,
            description="Controls randomness in text generation.",
        ),
    ]
    max_length: Annotated[
        int,
        Field(
            default=-1,
            ge=-1,
            le=4000,
            description="Maximum number of tokens in the output.",
        ),
    ]
    top_p: Annotated[
        float,
        Field(
            default=1.0,
            ge=0.0,
            le=1.0,
            description="Controls nucleus sampling for diversity.",
        ),
    ]
    top_k: Annotated[
        int,
        Field(
            default=50,
            ge=1,
            le=1000,
            description="Limits vocabulary scope for diversity.",
        ),
    ]
    repetition_penalty: Annotated[
        float,
        Field(
            default=1.0, ge=1.0, le=2.0, description="Penalty to discourage repetition."
        ),
    ]


# text: str =
# Field(..., min_length=1, max_length=4000, description="Input text for summarization.")
# translate: bool =
# Field(True, description="Flag to translate Hebrew text to English and also repose.")
# temperature: confloat(ge=0.0, le=1.0) =
# Field(0.5, description="Controls randomness in text generation.")
# max_length: conint(ge=-1, le=4000) =
# Field(100, description="Maximum number of tokens in the output.")
# top_p: confloat(ge=0.0, le=1.0) =
# Field(1.0, description="Controls nucleus sampling for diversity.")
# top_k: conint(ge=1, le=1000) =
# Field(50, description="Limits vocabulary scope for diversity.")
# repetition_penalty: confloat(ge=1.0, le=2.0) =
# Field(1.0, description="Penalty to discourage repetition.")

# text: str
# translate: bool = True  # Flag to translate Hebrew text to English and also repose
# temperature: float = 1.0  # Default is 1.0 for neutral randomness
# max_length: int = -1  # Default maximum length of tokens generated
# top_p: float = 1.0  # Default to 1.0 (no nucleus sampling)
# top_k: int = 50  # Default to 50 for balanced generation
# repetition_penalty: float = 1.0  # Default to no repetition penalty
