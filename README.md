
# 🕵️ AI Agent Developer Roadmap & Curriculum

> From Prompts to Production.
> 
> A rigorous, project-based learning path to mastering Autonomous AI Agents, RAG, and Multi-Agent Systems.

## 🗺️ The Roadmap Overview

This repository follows a structure designed to take you from **ML Foundations** to **Deployment**. We don't just use tools; we build the logic behind them.


| **Phase** | **Focus** | **Key Concepts** | **Project** |
| -- | -- | -- | -- |
| **I. The Cognitive Engine** | ML/DL Math, Transformers | Embeddings, Attention, Tokenization | 🔢 **Vector Search & LSTM Generator** |
| **II. The Body (Agency)** | Tools, Loops, RAG | ReAct Pattern, Function Calling, Vector DBs | 🕵️ **The Data Detective (RAG+Web)** |
| **III. The Architect** | Memory, Planning | Vector Stores, Reflection, Graph Search | 🧭 **The Long-Term Travel Planner** |
| **IV. Production** | Fine-Tuning, Ops, Eval | QLoRA, Docker, LLM-as-a-Judge | 🏭 **Agent-as-a-Service API** |
| **V. Capstone** | Multi-Agent Systems | Collaboration, Handoffs, Shared State | 🏢 **Virtual Software House** |


## 📂 Repository Structure

```
ai-agent-roadmap/
├── 01_foundations/
│   ├── 01_vector_math_search.ipynb    # Build semantic search from scratch
│   └── 02_transformer_anatomy.ipynb   # Visualize Attention & generate text
├── 02_agency_loops/
│   ├── 03_manual_react_loop.ipynb     # The "Thought-Action" loop in raw Python
│   └── 04_rag_and_tools.ipynb         # Connecting PDFs and Search APIs
├── 03_memory_planning/
│   ├── 05_infinite_memory.ipynb       # Summarization & Entity extraction
│   └── 06_hierarchical_planning.ipynb # Critique & Refine loops
├── 04_production/
│   ├── 07_finetune_json_mode.ipynb    # QLoRA for structured output
│   └── 08_deployment/                 # FastAPI + Docker example
└── capstone_software_house/           # Multi-Agent coding team

```

## 🚀 Getting Started

### Prerequisites

-   **Python Proficiency:** Decorators, Classes, Async/Await.
    
-   **API Access:** OpenAI API Key (or Anthropic/OpenRouter).
    
-   **Hardware:** A GPU is recommended for Phase 4 (Fine-tuning), but Google Colab Free Tier is sufficient for most modules.
    

### Installation

1.  **Clone the Repo:**
    
    ```
    git clone [https://github.com/yourusername/ai-agent-roadmap.git](https://github.com/yourusername/ai-agent-roadmap.git)
    cd ai-agent-roadmap
    
    ```
    
2.  **Set up Environment:**
    
    ```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    ```
    
3.  Environment Variables:
    
    Create a .env file:
    
    ```
    OPENAI_API_KEY="sk-..."
    TAVILY_API_KEY="tvly-..."  # For search tools
    
    ```
    

## 🧠 Key Frameworks & Libraries

We start **Vanilla**, then move to **Frameworks**.

-   **Core:** `numpy`, `pandas`, `pytorch`
    
-   **Vector DBs:** `chromadb`, `faiss-cpu`
    
-   **Orchestration:** `langchain`, `langgraph`
    
-   **Serving:** `fastapi`, `uvicorn`
    
-   **Fine-Tuning:** `peft`, `bitsandbytes`, `transformers`
    

## 🤝 Contribution & Study Group

This roadmap is open source. If you find a new paper on Agent Planning or a better way to implement Memory, open a PR!

**Suggested Reading Schedule:**

-   **Week 1-2:** Foundations & Math.
    
-   **Week 3-4:** Building Basic Agents (ReAct).
    
-   **Week 5-6:** Memory & RAG.
    
-   **Week 7-8:** Advanced Planning & Fine-Tuning.
    

## 📄 License

MIT
