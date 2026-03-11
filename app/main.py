from fastapi import FastAPI
from . import models
from .database import engine
from app.routers import banks,branches

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(banks.router)
app.include_router(branches.router)
