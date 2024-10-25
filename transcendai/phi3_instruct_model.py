import subprocess
from abc import ABC, abstractmethod
from typing import IO, Generator, List, Optional

# import os
from transcendai.logger_config import logger
from transcendai.schemas import SummarizeRequest
from transcendai.translation_logics import translate_to_hebrew


class LlamaHandlerBase(ABC):
    @abstractmethod
    def process_text(self, request: SummarizeRequest) -> Generator[str, None, None]:
        """Abstract function to process text for Llama modules."""
        pass


class LlamaHandler(LlamaHandlerBase):
    def __init__(self, model_path: str):
        """Initializing llama handler."""
        # self.model_path = model_path TODO
        self.model_path = "/home/lior/.cache/llama.cpp/Phi-3-mini-4k-instruct-q4.gguf"
        # self.llama_cli_path = os.path.join('/root/.cache/llama.cpp', 'llama-cli') TODO
        # self.llama_cli_path =
        # os.path.join(os.path.dirname(__file__), "llama.cpp", "llama-cli")
        self.llama_cli_path = "/home/lior/paz/llama.cpp/llama-cli"

    def build_command(self, request: SummarizeRequest) -> List[str]:
        """Building the full llama command ."""
        return [
            self.llama_cli_path,
            "-m",
            self.model_path,
            "-p",
            f"Please summarize the following text into 5 bullet points: {request.text}",
            "--temp",
            str(request.temperature),
            "--n_predict",
            str(request.max_length),
            "--top_p",
            str(request.top_p),
            "--top_k",
            str(request.top_k),
            "--repeat_penalty",
            str(request.repetition_penalty),
        ]

    def process_text(self, request: SummarizeRequest) -> Generator[str, None, None]:
        """Processing the request."""
        try:
            command = self.build_command(request)
            logger.info(f"Executing LLaMA command: {' '.join(command)}")

            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            yield from self.stream_output(process, translate=request.translate)
        except FileNotFoundError as e:
            logger.error(f"Command not found: {e}")
            yield f"Error: The command was not found - {e}\n"
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed with exit status {e.returncode}: {e}")
            yield f"Error: Command failed with exit status {e.returncode} - {e}\n"
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            yield f"Error: {str(e)}\n"

    @staticmethod
    def stream_output(
        process: subprocess.Popen[str], translate: bool = True
    ) -> Generator[str, None, None]:
        """Generate stream response."""

        def generator() -> Generator[str, None, None]:
            """Generating a stream of response data from process."""
            stdout: Optional[IO[str]] = process.stdout
            stderr: Optional[IO[str]] = process.stderr

            if stdout is None or stderr is None:
                logger.error("Process stdout or stderr is None.")
                yield "Error: Process stdout or stderr is None.\n"
                return

            try:
                while True:
                    line = stdout.readline()
                    if not line:
                        break
                    if translate:
                        try:
                            line = translate_to_hebrew(line)
                            logger.info("Translated text from Hebrew to English.")
                        except Exception as e:
                            logger.error(f"Translation error: {e}")
                            yield f"Error: {str(e)}\n"
                    yield f"{line}\n"
            except Exception as e:
                logger.error(f"Error in stream_output: {e}")
                yield f"Error: {str(e)}\n"
            finally:
                yield "\n"
                stdout.close()
                stderr.close()
                process.terminate()
                process.wait()
                logger.info("Subprocess finished.")

        return generator()
