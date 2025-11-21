# 🗂️ Phase 3: The Architect (Memory & Planning)

**Goal:** Move from one-off tasks to complex, long-running goals.

This phase teaches you how to build agents with sophisticated memory systems and hierarchical planning capabilities. These are essential for agents that need to maintain context over extended periods and tackle multi-step objectives.

## 📚 Modules Overview

### Module 5: Memory Systems

**Topics:**
- **Memory Types:** Short-term (Context window) vs. Long-term (Vector/SQL)
- **Management:** Summarization, Moving Window, Entity Memory
- **State:** Managing conversation history across sessions

**Project 5: "The Infinite Companion"**
- File: `05_infinite_memory.ipynb`
- **Objective:** A chatbot that "remembers" facts about you from weeks ago.
- **What You'll Build:**
  1. Implement **SummaryMemory**: Summarize old conversation parts
  2. Implement **Entity Store**: Extract and persist facts about users
  3. Session management: Load memory into system prompt
  4. Memory retrieval based on context

### Module 6: Advanced Planning

**Topics:**
- **Decomposition:** Breaking big goals into sub-tasks
- **Search:** Monte Carlo Tree Search (MCTS), Graph-based planning
- **Self-Correction:** Reflection and critique loops

**Project 6: "The Travel Planner"**
- File: `06_hierarchical_planning.ipynb`
- **Objective:** Plan a 7-day itinerary given a budget and interests.
- **What You'll Build:**
  1. **Plan Generation:** LLM creates high-level task breakdown
  2. **Critique Loop:** Second LLM reviews and challenges the plan
  3. **Refinement:** First LLM revises based on feedback
  4. **Multi-criteria optimization:** Balance budget, time, interests

## 🎯 Learning Outcomes

By the end of this phase, you will:
- Understand different memory architectures
- Implement conversation summarization
- Build entity extraction and tracking systems
- Create hierarchical planning systems
- Implement self-critique and refinement loops
- Handle multi-objective optimization

## 🚀 Getting Started

1. Complete Phases 1 and 2 (foundations are essential)
2. Ensure you have persistent storage available (SQLite works)
3. Start with `05_infinite_memory.ipynb`
4. Complete all exercises in order

## 📖 Recommended Prerequisites

- Completed Phase 2 (Agency Loops & RAG)
- Understanding of database basics (SQL)
- Familiarity with JSON data structures

## ⏱️ Estimated Time

- **Module 5:** 12-15 hours
- **Module 6:** 10-12 hours
- **Total:** 3-4 weeks (at 5-10 hours/week)

## 🔑 Key Concepts

### Memory Architecture

```
┌─────────────────────────────────────┐
│        Short-Term Memory            │
│    (Current conversation in         │
│     LLM context window)             │
└─────────────────────────────────────┘
              ↕
┌─────────────────────────────────────┐
│        Long-Term Memory             │
│                                     │
│  ┌──────────┐      ┌──────────┐   │
│  │  Vector  │      │  Entity  │   │
│  │   Store  │      │   Store  │   │
│  └──────────┘      └──────────┘   │
└─────────────────────────────────────┘
```

### Planning Loop

```
Goal → Plan → Critique → Refine → Execute
         ↑                  │
         └──────────────────┘
         (Self-correction loop)
```

These patterns enable agents to work on long-term objectives!
