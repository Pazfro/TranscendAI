"""Creating a Looger."""

import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Initialize logger
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)

# Log to file
file_handler = logging.FileHandler(log_dir / "app.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter for log messages
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s  - %(funcName)s - %(message)s"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)
