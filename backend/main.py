from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib
import logging

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

class URLRequest(BaseModel):
    url: str

cached_results = {}

@app.get("/")  # ✅ Added this route to fix the "Not Found" error
def home():
    return {"message": "AI Threat Intelligence System is running!"}

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

