from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    POSTGRES_URL: str = os.getenv("POSTGRES_URL", "postgresql+psycopg2://postgres:1234@postgres:5432/rag_db")

    KAFKA_BROKER: str = os.getenv("KAFKA_BROKER", "localhost:9092")
    KAFKA_INGEST_TOPIC: str = os.getenv("KAFKA_INGEST_TOPIC", "ingestion-trigger")
    KAFKA_COMPLETED_TOPIC: str = os.getenv("KAFKA_COMPLETED_TOPIC", "ingestion-completed")
    
    class Config:
        env_file = ".env"

# Create an instance of the Settings class
settings = Settings()