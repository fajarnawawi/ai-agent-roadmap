"""
Agent-as-a-Service: FastAPI deployment of RAG agent.
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import time
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Agent API",
    description="Production RAG agent with tool use",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=500, description="User question")
    context: Optional[str] = Field(None, description="Optional context")

    class Config:
        schema_extra = {
            "example": {
                "question": "What are the core components of an AI agent?",
                "context": None
            }
        }

class Source(BaseModel):
    type: str
    reference: str

class AnswerResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]
    processing_time: float
    timestamp: str

# Metrics storage (in production, use Prometheus)
metrics = {
    "requests_total": 0,
    "requests_success": 0,
    "requests_error": 0,
    "total_latency": 0.0
}

# Middleware for request tracking
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests and track metrics."""
    start_time = time.time()

    logger.info(f"Incoming request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)

        process_time = time.time() - start_time
        metrics["requests_total"] += 1
        metrics["total_latency"] += process_time

        if response.status_code < 400:
            metrics["requests_success"] += 1
        else:
            metrics["requests_error"] += 1

        logger.info(f"Request completed in {process_time:.2f}s - Status: {response.status_code}")

        return response

    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        metrics["requests_error"] += 1
        raise

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

# Metrics endpoint
@app.get("/metrics")
async def get_metrics():
    """Return service metrics."""
    avg_latency = (
        metrics["total_latency"] / metrics["requests_total"]
        if metrics["requests_total"] > 0
        else 0
    )

    return {
        "requests_total": metrics["requests_total"],
        "requests_success": metrics["requests_success"],
        "requests_error": metrics["requests_error"],
        "average_latency": round(avg_latency, 3),
        "uptime": "N/A"  # Implement with process start time
    }

# Main agent endpoint
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Process a question using the RAG agent.

    Returns answer with sources and metadata.
    """
    start_time = time.time()

    try:
        logger.info(f"Processing question: {request.question[:50]}...")

        # TODO: Import and use actual agent from Module 4
        # For now, return mock response

        # Simulated agent processing
        answer = f"Mock answer for: {request.question}"
        sources = [
            {"type": "document", "reference": "chunk_0"},
            {"type": "document", "reference": "chunk_1"}
        ]

        processing_time = time.time() - start_time

        return AnswerResponse(
            question=request.question,
            answer=answer,
            sources=[Source(**s) for s in sources],
            processing_time=round(processing_time, 3),
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

# Root endpoint
@app.get("/")
async def root():
    """API information endpoint."""
    return {
        "service": "AI Agent API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
