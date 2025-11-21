# 🧠 Phase 1: The Cognitive Engine (Foundations & Models)

**Goal:** Understand the "brain" of the agent before giving it a body.

This phase builds your understanding of the mathematical and deep learning foundations that power AI agents. You'll learn by implementing core concepts from scratch before using pre-built frameworks.

## 📚 Modules Overview

### Module 1: The Mathematical Bedrock

**Topics:**
- **Linear Algebra:** Vectors, Matrices, Dot Products (crucial for Embeddings)
- **Optimization:** Loss Functions, Gradient Descent
- **ML Basics:** Supervised vs. Reinforcement Learning (high-level)
- **Evaluation:** Precision, Recall, F1 (for classifiers)

**Project 1: "The Vector Search Engine"**
- File: `01_vector_math_search.ipynb`
- **Objective:** Build a semantic search system from scratch to understand how Agents "retrieve" knowledge.
- **What You'll Build:**
  1. Load a text dataset
  2. Convert text to vectors using a simple pre-trained model (Word2Vec or GloVe)
  3. Implement **Cosine Similarity** manually (using NumPy dot product)
  4. Create a function that takes a query and finds the "nearest neighbor" document

### Module 2: Deep Learning & The Transformer

**Topics:**
- **Architectures:** RNNs vs. LSTMs vs. Transformers
- **Mechanisms:** Self-Attention (Q, K, V), Positional Encoding
- **NLP:** Tokenization, Embeddings, Context Windows

**Project 2: "The Autocomplete Bot"**
- File: `02_transformer_anatomy.ipynb`
- **Objective:** Understand how LLMs predict the next token.
- **What You'll Build:**
  1. Build a small **LSTM** model in PyTorch to generate text character-by-character
  2. Visualize the "Attention Weights" of a small pre-trained Transformer (BERT/GPT-2) to see what words it focuses on
  3. Experiment with **Temperature** and **Top-K sampling** to see how randomness affects creativity

## 🎯 Learning Outcomes

By the end of this phase, you will:
- Understand how embeddings represent semantic meaning
- Know how to implement similarity search from scratch
- Comprehend the Transformer architecture and attention mechanism
- Be able to generate text using neural language models
- Grasp the fundamental concepts that power modern LLMs

## 🚀 Getting Started

1. Ensure you have the required dependencies installed (see root `requirements.txt`)
2. Start with `01_vector_math_search.ipynb`
3. Complete all exercises in order
4. Experiment with different parameters and datasets

## 📖 Recommended Prerequisites

- Python fundamentals (numpy, pandas)
- Basic understanding of machine learning concepts
- Familiarity with Jupyter notebooks

## ⏱️ Estimated Time

- **Module 1:** 8-12 hours
- **Module 2:** 10-15 hours
- **Total:** 2-3 weeks (at 5-10 hours/week)
