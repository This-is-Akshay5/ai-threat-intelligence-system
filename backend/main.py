from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import hashlib
import logging
import os

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Serve static frontend files
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    """ Serves the frontend HTML file """
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"error": "Frontend not found"}

# ✅ URL Analysis API
class URLRequest(BaseModel):
    url: str

cached_results = {}

@app.post("/analyze")
async def analyze_url(request: URLRequest):
    try:
        url_hash = hashlib.sha256(request.url.encode()).hexdigest()

        if url_hash in cached_results:
            return cached_results[url_hash]

        # Simulated threat score logic (Replace with real AI detection)
        threat_score = sum(ord(c) for c in request.url) % 100

        result = {
            "url": request.url,
            "threat_score": threat_score
        }

        cached_results[url_hash] = result

        return result

    except Exception as e:
        logger.error(f"Error analyzing URL {request.url}: {str(e)}")
        return {"error": "Internal Server Error"}
