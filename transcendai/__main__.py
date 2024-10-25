import uvicorn

from transcendai.rest_api import app

if __name__ == "__main__":
    """Initializing rest api."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
