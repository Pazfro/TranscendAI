"""Main initializing the fast api."""

import uvicorn

from transcendai.rest_api import app

if __name__ == "__main__":
    """Starting the fast api."""
    uvicorn.run(app, host="127.0.0.1", port=8000)
