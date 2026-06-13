import os
from pathlib import Path


PROJECT_TYPE = 'Simple RAG'
PROJECT_SUBJECT = 'Hotel SOP Knowledge Assistant with FastAPI, React, ChromaDB, PostgreSQL, Docker'
DIFFICULTY_LEVEL = 'Advanced'
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "sample_docs"
CHROMA_DIR = BASE_DIR / ".chroma"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")
