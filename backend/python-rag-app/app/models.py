from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from pgvector.sqlalchemy import Vector
from pydantic import BaseModel
from typing import List, Dict, Any

Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filepath = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    document_metadata = Column(JSONB, nullable=True)  # Renamed from metadata to document_metadata
    embedding = Column(Vector, nullable=True)  # Example of using the Vector type

# Pydantic schemas
class Message(BaseModel):
    role: str
    content: str

class DocumentIngestRequest(BaseModel):
    filepath: str
    filename: str

class GenerateRequest(BaseModel):
    query: str
    chat_history: List[Message]
    use_knowledge_base: bool = True

class SearchRequest(BaseModel):
    content: str

class DocumentResponse(BaseModel):
    source: str
    content: str

