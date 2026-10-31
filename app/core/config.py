from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = "IT Helpdesk Agentic RAG"
    app_env: str = "development"
    google_api_key: str = ""
    tavily_api_key: str = ""
    pinecone_api_key: str = ""
    pinecone_index_name: str = "it-helpdesk-agentic-rag"
    pinecone_namespace: str = "it-helpdesk-kb"
    embedding_model: str = "gemini-embedding-001"
    gemini_model: str = "gemini-3.8-flash"
    top_k: int = 4
    max_retries: int = 1
    admin_api_key: str = "change-me"
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")

    model_config= SettingsConfigDict(env_file=str(BASE_DIR/".env"),extra="ignore")

@lru_cache
def get_settings()->Settings:
    return Settings()