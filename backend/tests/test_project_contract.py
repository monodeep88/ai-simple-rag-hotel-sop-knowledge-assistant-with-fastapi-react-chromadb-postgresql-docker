from pathlib import Path

from app.config import DIFFICULTY_LEVEL, PROJECT_SUBJECT, PROJECT_TYPE
from app.services.pipeline import run_pipeline
from app.services.text import split_text
from app.services.tools import calculate


def test_project_metadata():
    assert PROJECT_TYPE == 'Simple RAG'
    assert PROJECT_SUBJECT == 'Hotel SOP Knowledge Assistant with FastAPI, React, ChromaDB, PostgreSQL, Docker'
    assert DIFFICULTY_LEVEL == 'Advanced'


def test_text_splitter_creates_chunks():
    chunks = split_text("hello world " * 200, chunk_size=120, overlap=20)
    assert len(chunks) > 1


def test_calculator_tool():
    assert calculate("1 + 2 * 3") == "7"


def test_pipeline_returns_answer_sources_and_steps():
    result = run_pipeline("What is the refund policy?")
    assert result.answer
    assert result.sources
    assert result.steps
    assert result.project_type == 'Simple RAG'


def test_full_stack_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "App.jsx").exists()
    assert (root / "backend" / "app" / "main.py").exists()
    assert (root / "docker-compose.yml").exists()
