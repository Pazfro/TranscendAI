import os
from pathlib import Path

import pytest

from transcendai.phi3_instruct_model import LlamaHandler
from transcendai.schemas import SummarizeRequest


@pytest.fixture
def llama_handler():
    """Create llama handler.

    make sure env LLAMA_CLI_PATH is configured
    """
    home_dir = Path.home()
    return LlamaHandler(
        model_path=os.path.join(
            home_dir, ".cache", "llama.cpp", "Phi-3-mini-4k-instruct-q4.gguf"
        )
    )


def test_command_generation(llama_handler):
    """Testing correct command generation."""
    request = SummarizeRequest(text="Test input", temperature=0.5, max_length=100)
    command = llama_handler.build_command(request)
    assert command[3:] == [
        "-p",
        "Please summarize the following text into 5 bullet points: Test input",
        "--temp",
        "0.5",
        "--n_predict",
        "100",
        "--top_p",
        "1.0",
        "--top_k",
        "50",
        "--repeat_penalty",
        "1.0",
    ]
