from fastapi import FastAPI
from app.routers import books


app = FastAPI(title="FastAPI + Docker + Postgres")

app.include_router(books.router)

# Base.metadata.create_all(bind=engine)

