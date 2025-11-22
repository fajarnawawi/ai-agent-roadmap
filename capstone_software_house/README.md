# 🏢 Capstone: Virtual Software House

**The Ultimate Challenge:** Build a multi-agent system that writes software autonomously.

## 🎯 Objective

Create a system where three specialized agents collaborate to:
1. Understand a product idea
2. Write specifications
3. Implement code
4. Review and fix bugs

## 🤖 The Agents

### 1. Product Manager Agent
**Role:** Requirements gathering and specification

**Responsibilities:**
- Takes user's high-level idea
- Asks clarifying questions
- Writes detailed technical specification
- Defines success criteria

**Output:** `spec.md` file

### 2. Developer Agent
**Role:** Code implementation

**Responsibilities:**
- Reads the specification
- Writes Python code
- Adds documentation and type hints
- Creates test cases

**Output:** `main.py`, `tests.py`

### 3. Reviewer Agent
**Role:** Quality assurance

**Responsibilities:**
- Runs the code
- Checks for errors and bugs
- Runs tests
- Sends feedback to Developer if issues found

**Output:** `review.md`, approval/rejection

## 🏗️ Architecture

```
User Idea
    ↓
┌─────────────────────┐
│  Product Manager    │ → spec.md
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Developer          │ → main.py, tests.py
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Reviewer           │ → Execute & Test
└─────────────────────┘
    ↓
  Pass? → ✅ Done
    ↓
  Fail? → 🔁 Back to Developer
```

## 📁 Project Structure

```
capstone_software_house/
├── README.md                 # This file
├── main.py                   # Orchestrator
├── agents/
│   ├── __init__.py
│   ├── product_manager.py   # PM agent
│   ├── developer.py          # Dev agent
│   └── reviewer.py           # QA agent
├── workspace/                # Shared filesystem
│   ├── spec.md
│   ├── main.py
│   └── tests.py
└── examples/
    └── sample_projects.md    # Example ideas to test
```

## 🚀 Usage

```python
from main import SoftwareHouse

# Initialize the system
house = SoftwareHouse()

# Give it an idea
idea = "Create a command-line todo list app with add, list, and remove commands"

# Let agents build it
result = house.build(idea)

# Get the generated code
print(result['code'])
```

## 🎯 Learning Goals

By completing this capstone, you will:

1. **Multi-Agent Coordination:** Manage handoffs between agents
2. **Shared State:** Implement a "filesystem" for agents to read/write
3. **Feedback Loops:** Handle iterative refinement
4. **Error Handling:** Gracefully handle code execution failures
5. **End-to-End Automation:** Build a complete autonomous system

## 💡 Extension Ideas

1. **Version Control Agent:** Tracks changes, creates git commits
2. **Documentation Agent:** Writes README and API docs
3. **Deployment Agent:** Containerizes and deploys the app
4. **User Feedback Agent:** Simulates user testing
5. **Multiple Languages:** Support JavaScript, Go, etc.

## 🏆 Success Criteria

Your system should be able to:
- ✅ Generate working code from natural language
- ✅ Write its own test suite
- ✅ Debug and fix simple errors autonomously
- ✅ Handle at least 3 different project types
- ✅ Complete the process in < 5 minutes

## 📝 Example Projects

See `examples/sample_projects.md` for ideas to test:
- Calculator CLI
- File organizer
- Web scraper
- Data analyzer
- API client

## 🎓 What You've Learned

This capstone synthesizes **everything** from the curriculum:

- **Phase 1:** LLM fundamentals (generation, prompting)
- **Phase 2:** Tool use (code execution, file I/O)
- **Phase 3:** Memory (conversation history, state management)
- **Phase 4:** Production (error handling, logging, optimization)

You're now ready to build **real-world AI agent systems**!

---

**Next Steps:**
1. Read through the starter code
2. Implement each agent in `agents/`
3. Test with simple projects first
4. Gradually increase complexity
5. Share your results! 🎉
