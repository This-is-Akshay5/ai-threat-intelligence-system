from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

cached_results = {}

@app.post("/analyze")
async def analyze_url(request: URLRequest):
    url_hash = hashlib.md5(request.url.encode()).hexdigest()

    if url_hash in cached_results:
        return cached_results[url_hash]

    # Simulated threat score logic
    threat_score = sum(ord(c) for c in request.url) % 100

    result = {
        "url": request.url,
        "threat_score": threat_score
    }

    cached_results[url_hash] = result

    return result
