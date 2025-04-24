
from fastapi import FastAPI
from dashboard.backend.router import router
app = FastAPI()
app.include_router(router)
    