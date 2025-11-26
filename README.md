# A03-Career-Mentor-AI-Agent
Built an adaptive AI career-planning agent using LangChain and GPT models; designed for job seekers transitioning into tech.

# Career Mentor AI – Course Project (AI Agent)

This repository contains my course project for building a working AI Agent.  
The agent is designed to help early-career professionals and students create personalized learning roadmaps for careers in software engineering or related technical fields.

---

## 🚀 Project Overview

**Career Mentor AI** is an AI-powered career planning assistant that:

- Collects user background, goals, and available study time  
- Generates a personalized learning roadmap  
- Retrieves curated learning resources using RAG (Retrieval-Augmented Generation)  
- Adapts recommendations based on user feedback and progress  

This project fulfills the course requirements to design, build, and demonstrate a functional AI agent aligned with real-world needs.

---

## 🧠 Key Features

- **RAG-powered recommendations** using ChromaDB  
- **Personalized learning plan generation**  
- **Agent workflow designed with LangChain**  
- **Easy-to-use UI created with Streamlit**  
- **Hybrid architecture with reasoning + memory + retrieval**  

---

## 🏗️ Tech Stack

- **LangChain** – Agent orchestration  
- **FastAPI** – Backend API  
- **Streamlit** – UI for user interaction  
- **ChromaDB** – Vector database for resource retrieval  
- **Python** – Core implementation  

---

## 📊 System Workflow Diagram

See: `workflow_diagram.png` 

---

## 📄 Project Files
ai-agent-project/
│
├── Part_1_Report.md
├── workflow_diagram.png
├── src/
│ └── agent_app.py
├── requirements.txt
└── README.md


---

## 🎥 Walkthrough Video
 
*To be added after recording*

---

## 📘 Part 1 Report 
👉 `Part_1_Report.md`

---

## ▶️ How to Run the Agent

### 1. Install dependencies
`pip install -r requirements.txt`

### 2. Start the API backend
`uvicorn src.agent_app:app --reload`

---

## 💡 Author
Junlin Li  
Course Project – AI Agent Development  
2025
