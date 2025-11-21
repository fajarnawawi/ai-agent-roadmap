# 🛠️ Phase 2: The Body (Action & Tools)

**Goal:** Break the LLM out of the text box. Make it "do" things.

This phase teaches you how to build AI agents that can interact with the world through tools and APIs. You'll start by building everything from scratch (no frameworks!) before moving to production-ready patterns.

## 📚 Modules Overview

### Module 3: The Agency Loop (Reasoning)

**Topics:**
- **Prompt Engineering:** Chain-of-Thought (CoT), Tree-of-Thought
- **Agent Patterns:** ReAct (Reason + Act), MRKL
- **Parsing:** Extracting structured actions (JSON) from unstructured text

**Project 3: "The Hard-Coded Agent"**
- File: `03_manual_react_loop.ipynb`
- **Objective:** Build an Agent loop **without** frameworks (No LangChain).
- **What You'll Build:**
  1. Define two Python functions: `get_weather(city)` and `calculator(expression)`
  2. Write a System Prompt that forces the LLM to output: `THOUGHT: ... ACTION: ...`
  3. Write a Python `while` loop that:
     - Sends prompt to LLM
     - RegEx parses the `ACTION`
     - Executes the Python function
     - Feeds the result back to the LLM as `OBSERVATION`

### Module 4: Tool Integration & RAG

**Topics:**
- **RAG:** Retrieval Augmented Generation, Vector Databases (Chroma/Pinecone)
- **Tool Use:** APIs, Web Browsing, File I/O
- **Orchestration:** Connecting retrieval to generation

**Project 4: "The Data Detective"**
- File: `04_rag_and_tools.ipynb`
- **Objective:** An agent that can query a PDF and verify facts on Wikipedia.
- **What You'll Build:**
  1. Ingest a PDF report into a Vector Store (Chunking + Embedding)
  2. Create a `search_wikipedia` tool wrapper
  3. Build a **Router Chain**: The agent decides "Do I look in the PDF, or do I search the web?" based on the question
  4. **Output:** A final answer citing sources from both the PDF and the Web

## 🎯 Learning Outcomes

By the end of this phase, you will:
- Understand the ReAct (Reasoning + Acting) pattern
- Know how to build agent loops from scratch
- Implement RAG (Retrieval Augmented Generation)
- Connect LLMs to external tools and APIs
- Build routing logic for multi-tool agents
- Understand when to use retrieval vs direct generation

## 🚀 Getting Started

1. Complete Phase 1 first (foundations are essential)
2. Ensure you have an OpenAI API key set in `.env`
3. Start with `03_manual_react_loop.ipynb`
4. Complete all exercises in order

## 📖 Recommended Prerequisites

- Completed Phase 1 (Vector Search & Transformers)
- Understanding of LLM APIs (OpenAI, Anthropic, etc.)
- Basic regex knowledge
- Familiarity with REST APIs

## ⏱️ Estimated Time

- **Module 3:** 10-12 hours
- **Module 4:** 12-15 hours
- **Total:** 3-4 weeks (at 5-10 hours/week)

## 🔑 Key Concepts

### The ReAct Pattern

```
THOUGHT: I need to find the weather in London
ACTION: get_weather("London")
OBSERVATION: 15°C, Cloudy
THOUGHT: Now I can answer the user
ANSWER: The weather in London is 15°C and cloudy.
```

### RAG Architecture

```
User Query → Embedding → Vector Search → Retrieve Docs → LLM + Context → Answer
```

These patterns are the foundation of modern AI agents!
