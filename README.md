# 🚀 Multi-Agent AI Software Engineering Team Simulator

> A stateful multi-agent system that simulates a real software development team (Product Manager → Tech Lead → Developer → QA) collaborating to iteratively design and refine high-quality technical plans.

---

# 🧠 Overview

This project demonstrates how autonomous AI agents can coordinate like a real engineering organization.

Given a product goal, the system:

1. Breaks the goal into structured development tasks
2. Refines tasks into engineering architecture
3. Generates detailed implementation plans
4. Critiques solutions using a QA agent
5. Iteratively improves output using scoring feedback
6. Detects convergence based on quality thresholds
7. Persists shared memory across runs

This is not simple prompt chaining.

It is a structured multi-agent workflow with:

- Role specialization
- Iterative feedback loops
- Convergence logic
- Persistent shared memory
- Cross-run learning

---

# 🏗️ System Architecture

```
                USER GOAL
                    │
                    ▼
         ┌────────────────────┐
         │  Product Manager   │
         └────────────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │     Tech Lead      │
         └────────────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │     Developer      │
         └────────────────────┘
                    │
                    ▼
         ┌────────────────────┐
         │        QA          │
         └────────────────────┘
                    │
         Iterative Critic Loop
                    │
                    ▼
             Convergence Logic
                    │
                    ▼
              Final Plan Output
```

---

# 👥 Agent Roles

## 📌 Product Manager Agent

- Converts high-level goal into structured development tasks
- Focuses on scope, features, and user needs

## 🏗️ Tech Lead Agent

- Refines tasks into technically clear deliverables
- Proposes architecture
- Identifies risks and missing considerations

## 💻 Developer Agent

- Selects a task
- Generates step-by-step implementation plan
- Suggests tech stack
- Estimates complexity

## 🔍 QA / Critic Agent

- Reviews developer plan
- Assigns quality score (1–10)
- Identifies weaknesses
- Suggests concrete improvements
- Decides APPROVE or REVISE

---

# 🔁 Iterative Improvement Engine

The system simulates real engineering iteration:

```
Developer Plan → QA Review → Score → Revision → QA Review → ...
```

The loop stops when:

- A quality threshold is reached
- Improvement plateaus
- Maximum iterations are reached

This models real-world design refinement cycles.

---

# 🧠 Shared Memory System

A persistent memory layer stores:

- Current run ID
- Product goal
- PM output
- Architecture suggestions
- Identified risks
- Developer versions
- QA reviews
- Critic scores
- Iteration history
- Full timestamped change log

Memory persists across runs, enabling cross-session learning.

Previous QA feedback can influence future planning cycles.

---

# 📂 Project Structure

```
multi-agent-ai-team/
│
├── agents/
│   ├── product_manager.py
│   ├── tech_lead.py
│   ├── developer.py
│   ├── qa.py
│
├── memory/
│   ├── memory_store.py
│
├── orchestrator.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Tech Stack

- Python
- Gemini API (LLM backbone)
- JSON-based persistent memory
- Multi-agent orchestration
- Prompt-driven role simulation

Concepts Demonstrated:

- Agent collaboration
- State management
- Iterative self-improvement
- Convergence detection
- Structured prompt engineering
- Architecture reasoning

---

# ▶️ How It Works (Execution Flow)

1. User provides product goal
2. PM converts goal → task list
3. Tech Lead refines → architecture + risks
4. Developer generates implementation plan
5. QA reviews and assigns score
6. Developer revises using feedback
7. Loop continues until convergence

Final output includes:

- Refined technical plan
- Iteration history
- Final critic evaluation

---

# ▶️ How To Run

## 1) Clone Repository

```
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```

## 2) Install Dependencies

```
pip install -r requirements.txt
```

## 3) Add API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_key_here
```

## 4) Run

```
python main.py
```

Provide a product goal when prompted.

Example:

```
Build an AI-powered personal finance assistant that predicts cash flow and detects unusual spending.
```

---

# 📊 Example Capabilities

The system can generate:

- Structured product task breakdown
- Microservice-level architecture proposals
- Database schema suggestions
- ML pipeline design
- Security strategy planning
- CI/CD and deployment strategies
- Risk assessment and mitigation plans

---

# 💡 Why This Project Is Different

Most AI demos are single-prompt systems.

This project demonstrates:

- Multi-agent coordination
- Structured engineering simulation
- Iterative quality improvement
- Persistent system memory
- Convergence-based stopping criteria

It reflects systems-level thinking rather than isolated LLM usage.

---

# 🧩 Future Extensions

Potential upgrades:

- Code-generation agent
- Tool-using agents
- Retrieval-augmented memory
- Automatic GitHub PR creation
- Execution benchmarking
- Performance analytics dashboard

---

# 🎯 Purpose

This project explores how AI agents can simulate structured software engineering workflows and collaboratively improve technical plans through iterative critique and refinement.

It is designed as a systems-thinking portfolio project demonstrating advanced LLM orchestration.

---

# ⭐ If You Found This Interesting

Star the repository and explore multi-agent AI systems further.
