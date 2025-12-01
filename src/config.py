import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = "text-embedding-3-small"
    CHROMA_DB_PATH = "./chroma_db"
    RETRIEVE_COUNT = 3

    LLM_MODEL = GROQ_MODEL