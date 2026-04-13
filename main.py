import logging
from fastapi import FastAPI, logger
from routers.tasks_base import router as tasks_base_router
from middleware import setup_logging_middleware

app = FastAPI()
app.include_router(tasks_base_router)



setup_logging_middleware(app)

#Funzione con decorator @app.get("/health") che definisce un endpoint GET /health.
# deve darti un messaggio nel terminale di tipo logger:
#2026-04-09 10:30:00 | INFO | main | Health check called
#mentre ritorna sull'endpoint {"status": "ok"}
@app.get("/health")
def health_check():
    return {"status": "ok"}
