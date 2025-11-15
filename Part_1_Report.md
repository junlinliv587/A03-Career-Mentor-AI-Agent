Part 1 – Design and Plan Your AI Agent Workflow
1. Reflect on Your Agent Idea

Agent Name: Career Mentor AI

User Problem:
Many early-career professionals and career changers struggle to identify a clear, structured learning roadmap aligned with their goals in tech. They often waste time finding reliable resources or understanding which skills are most relevant to their target jobs.

Target Domain:
Career development and personalized learning guidance for aspiring software engineers or technology professionals.

Core Capabilities:

Gather user background information (skills, goals, learning time).

Generate a personalized learning roadmap using AI reasoning and retrieval.

Recommend curated learning materials (courses, GitHub projects, tutorials).

Adapt recommendations based on user feedback and progress.

Value Delivered:
Career Mentor AI reduces the time and uncertainty of planning a self-learning path, helping users transition efficiently into technical roles through structured, adaptive, and evidence-based guidance.

2. Framework, Architecture & Design Pattern

Framework Choice:

LangChain – for orchestration of LLM reasoning, memory, and retrieval.

FastAPI + Streamlit – FastAPI serves as the backend API; Streamlit provides a lightweight UI for interactions.

ChromaDB – for vector storage of career guides, curricula, and learning resources.

Design Pattern:

Retrieval-Augmented Generation (RAG) with memory. The agent retrieves relevant content from a custom career knowledge base and integrates it with LLM reasoning to produce personalized responses.

Architecture:

Hybrid Layered Architecture including:

User Interface Layer (Streamlit) – handles input/output.

Processing Layer (LangChain Reasoning Engine) – performs prompt parsing, context building, and reasoning.

Retrieval Layer (ChromaDB + Embeddings) – fetches relevant career resources.

Memory Layer – tracks user preferences and progress.

Justification:
This stack offers strong modularity and adaptability with minimal code complexity. LangChain’s components allow plug-and-play reasoning and retrieval, while Streamlit makes it easy to demonstrate a working prototype without front-end development.

3. Map the Workflow
Component	Function	Input / Output	Notes
User Input Parser	Collect background and career goals	User text (e.g., “I want to be a backend developer in 1 year”)	Extracts skills, time frame, target role
Reasoning Module (LLM Chain)	Plan learning steps and goals	Parsed intent → structured plan	Uses templates and LLM reasoning
Retriever Module (ChromaDB)	Fetch relevant resources	Query → list of resources	RAG knowledge retrieval step
Response Formatter	Summarize and output plan	Structured data → Readable text or table	Produces career roadmap and links
Memory / Feedback Loop	Adapt to progress and feedback	User feedback → adjusted plan	Optional for future improvement

Optional Features:

Personalized learning recommendations based on previous queries.

Confidence score for each resource recommendation.

Feedback loop for continuous adaptation.

4. Visualize the Agent

Your system diagram should illustrate this flow:

[User Input]
    ↓
[Input Parser]
    ↓
[Reasoning Engine (LangChain)]
    ↙           ↘
[Vector DB (ChromaDB)]   [Memory Store]
    ↓
[Response Formatter]
    ↓
[Streamlit Output UI]

This diagram shows the end-to-end interaction: the user submits their career goal; the agent retrieves contextual learning resources, reasons through the plan, and returns a customized learning roadmap.
