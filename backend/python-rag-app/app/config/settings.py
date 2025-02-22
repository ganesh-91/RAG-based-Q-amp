import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:1234@postgres:5432/rag_db")

    KAFKA_BROKER: str = os.getenv("KAFKA_BROKER", "localhost:9092")
    KAFKA_INGEST_TOPIC: str = os.getenv("KAFKA_INGEST_TOPIC", "ingestion-trigger")
    KAFKA_COMPLETED_TOPIC: str = os.getenv("KAFKA_COMPLETED_TOPIC", "ingestion-completed")

    class Config:
        env_file = ".env"

settings = Settings()