# ⚙️ Phase 4: Production & Specialization

**Goal:** Optimize, serve, and scale AI agents for production use.

This phase covers fine-tuning models for specialized tasks, deploying agents as services, and implementing proper evaluation and monitoring.

## 📚 Modules Overview

### Module 7: Fine-Tuning & Optimization

**Topics:**
- **PEFT/LoRA:** Parameter-Efficient Fine-Tuning
- **Quantization:** 4-bit/8-bit model loading (QLoRA)
- **Instruction Tuning:** Training models for specific agent behaviors
- **Evaluation:** Measuring fine-tuned model performance

**Project 7: "The JSON Specialist"**
- File: `07_finetune_json_mode.ipynb`
- **Objective:** Fine-tune a small model (Llama-3-8B or Mistral) to **always** output valid JSON.
- **What You'll Build:**
  1. Curate a dataset of (User Query) → (JSON Action) pairs
  2. Use **QLoRA** to fine-tune a base model efficiently
  3. Benchmark against base model on syntax errors
  4. Test with various structured output tasks

### Module 8: Ops, Deployment & Evaluation

**Topics:**
- **Serving:** FastAPI, async request handling
- **Evaluation:** LLM-as-a-Judge, RAGAS metrics (Faithfulness, Answer Relevancy)
- **Safety:** Guardrails, prompt injection defense
- **Monitoring:** Token usage, latency, error rates

**Project 8: "Agent-as-a-Service"**
- Directory: `08_deployment/`
- **Objective:** Deploy the "Data Detective" from Module 4 as a production API.
- **What You'll Build:**
  1. Wrap agent logic in **FastAPI** endpoint
  2. Add LangSmith or Arize Phoenix traces for monitoring
  3. Build test suite with "Judge LLM" for answer quality
  4. Dockerize the service
  5. Implement rate limiting and error handling

## 🎯 Learning Outcomes

By the end of this phase, you will:
- Understand parameter-efficient fine-tuning (LoRA, QLoRA)
- Be able to fine-tune models for specific agent tasks
- Deploy agents as production REST APIs
- Implement comprehensive evaluation pipelines
- Monitor and debug production agent systems
- Apply safety guardrails and input validation

## 🚀 Getting Started

1. **For Module 7 (Fine-tuning):**
   - GPU recommended (Google Colab T4 sufficient)
   - Hugging Face account for model access
   - Understanding of PyTorch basics

2. **For Module 8 (Deployment):**
   - Docker installed
   - Basic understanding of REST APIs
   - Familiarity with async Python

## ⏱️ Estimated Time

- **Module 7:** 15-20 hours
- **Module 8:** 12-15 hours
- **Total:** 4-5 weeks (at 5-10 hours/week)

## 🔑 Key Concepts

### LoRA/QLoRA

```
Full Fine-Tuning:  Update ALL 7B parameters 💰💰💰
LoRA:              Update ~0.1% via low-rank adapters 💰
QLoRA:             LoRA + 4-bit quantization 💵
```

### Production Architecture

```
User Request
     ↓
[Load Balancer]
     ↓
[FastAPI Service] ← Monitoring
     ↓
[Agent Logic]
     ↓
[LLM + Tools]
     ↓
Response + Traces
```

## 📖 Recommended Prerequisites

- Completed Phases 1-3
- Python async/await understanding
- Basic Docker knowledge (for Module 8)
- GPU access (for Module 7, or use Colab)

This is where agents become **production-ready**!
