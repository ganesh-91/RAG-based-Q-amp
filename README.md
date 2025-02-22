# RAG-based Q&A Web Application

This project is a **Retrieval-Augmented Generation (RAG)**-based Q&A web application, showcasing a microservice architecture for an intelligent question-answering system. It integrates **React** for the frontend, **NestJS (Node.js)** for authentication and document management, **Postgre** for storing vector embeddings and **Python** for LLM-based document retrieval.

## Key Features
- **User Authentication** via secure login/signup system.
- **Document Upload and Management** for ingestion of new documents.
- **RAG-based Q&A** utilizing large language models to retrieve relevant answers.
- **Microservice Architecture** using **Kafka** for seamless inter-service communication.

## Tech Stack
- **Frontend**: React
- **Vector Database**: Postgres
- **Backend**: 
  - **NestJS (Node.js)** for authentication and document management.
  - **Python** (FastAPI) for retrieval-augmented generation (RAG).
- **Messaging**: Kafka for distributed communication between services.

## System Architecture

- **Authentication**  
  `Frontend (React)` → `Backend (NestJS)`

- **Document Upload**  
  `Frontend (React)` → `Backend (NestJS)`

- **Document Ingestion**  
  `Frontend (React)` → `Backend (NestJS)` → `Kafka Queue` → `Backend (Python RAG Service)`

- **Saving Vector Ingestion**  
  `Backend (NestJS)` → `Postgres`

- **Question and Answer Flow**  
  `Frontend (React)` → `Backend (Python RAG Service)`

## Getting Started

### Prerequisites
Before you begin, make sure you have the following installed:
- Node.js (v18 or higher)
- Python (v3 or higher)
- Kafka
- Postgres
- Docker (for Docker setup)

### Local Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/RAG-based-QA-Application.git

2. **Set up Kafka**
Follow this guide to set up Kafka: Kafka Connect Quickstart - https://medium.com/walmartglobaltech/kafka-connect-quickstart-71c8a70bc454.

3. **Setup Postgres and postgres vector plugin**
- Download and install postgres from - https://www.postgresql.org/download
- Install pgvector by following the steup mnetioned in the git repo -https://github.com/pgvector/pgvector

5. **Backend Setup (NestJS - Authentication and Document Management)**
   ```bash
   cd backend/nest-auth-app
   npm install
   npm run start:dev

6. **Backend Setup (Python RAG Service)**
   ```bash
   cd backend/python-rag-app
   pip install -r requirements.txt
   uvicorn app.main:app --reload

7. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm start

### Running with Docker
For a streamlined setup using Docker, simply run:
   ```bash
   docker-compose up --build
   ```

This will spin up all the necessary services in Docker containers, including the Kafka service, backend services, and the frontend.

### How It Works
- **Authentication**: Users can securely sign in or register, with authentication handled by the NestJS backend.
- **Document Upload**: Users can upload documents, which are processed by the NestJS service and queued for ingestion via Kafka.
- **Ingestion Process**: Kafka ensures efficient data flow by passing document data from the NestJS backend to the Python RAG service for processing.
- **Q&A System**: Users can ask questions related to the ingested documents, with answers retrieved and generated by the Python-based RAG service.

### Future Enhancements
- Enhancing document ingestion with more **formats and metadata** extraction.
- Integrating **advanced LLM models** for even more accurate and context-aware answers.
