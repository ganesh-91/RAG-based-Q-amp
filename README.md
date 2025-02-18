# RAG-based-Q-A-Application

## App Architecture

For Authentication
Frontent app -> Nest js app

Document upload 
Frontend -> Nest js app

For ingestion 
Frontend -> Nest js -> kafka q -> Python rag app

QandA 
Frontend -> Python rag app

## Setup

For normal setup-

> 1. Clone the repo.
>
> 2. Setup kafka and run it
>   
>    a. cd backend/nest-auth-app
>    
>    b. npm install
>
>    c. npm run start:dev
>
> 3. cd backend/python-rag-app
>   
>    a. pip install -r requirement.txt
>    b. uvicorn app.main:app --reload
>
> 4. cd frontend
>   
>    a. npm i
>
>    b.npm start

For docker -
> run docker-compose up --build
 
