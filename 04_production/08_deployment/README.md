# 🚀 Project 8: Agent-as-a-Service

Deploy the RAG agent from Module 4 as a production-ready API.

## 🎯 What You'll Build

A complete production deployment including:
- FastAPI REST endpoint
- Request/response validation
- Error handling and logging
- Rate limiting
- Monitoring and tracing
- Docker containerization
- Health checks

## 📁 Files

- `main.py` - FastAPI application
- `agent.py` - Agent logic from Module 4
- `Dockerfile` - Container configuration
- `docker-compose.yml` - Service orchestration
- `requirements.txt` - Python dependencies
- `test_api.py` - Integration tests
- `.env.example` - Environment variables template

## 🚀 Quick Start

1. **Setup Environment:**
   ```bash
   cp .env.example .env
   # Add your API keys to .env
   ```

2. **Run Locally:**
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. **Run with Docker:**
   ```bash
   docker-compose up --build
   ```

4. **Test:**
   ```bash
   curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the core components of an AI agent?"}'
   ```

## 📊 Monitoring

Access at:
- API Docs: http://localhost:8000/docs
- Health: http://localhost:8000/health
- Metrics: http://localhost:8000/metrics

## 🔑 Key Features

- **Async Processing:** Non-blocking request handling
- **Input Validation:** Pydantic models
- **Rate Limiting:** Per-user quotas
- **Caching:** Response caching for common queries
- **Logging:** Structured JSON logs
- **Metrics:** Request count, latency, errors
