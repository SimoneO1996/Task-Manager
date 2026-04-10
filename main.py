import logging
from fastapi import FastAPI
from routers.tasks_base import router as tasks_base_router

app = FastAPI()
app.include_router(tasks_base_router)

from middleware import setup_logging_middleware
setup_logging_middleware(app)


# mostra i messaggi di log nel terminale 
# %(asctime)s  è il timestamp, 
# %(levelname)s → livello tipo info, warning, error o altro.
# %(name)s → nome di chi logga 
# %(message)s il messaggio che scrivi tu in questo caso dato dal decorator 
#datefmt="%Y-%m-%d %H:%M:%S" è il formato del timestamp (2026-04-09 10:30:00)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
#logger = logging.getLogger(__name__) crea un logger specifico per questo file
#__name__ è una variabile Python che vale il nome del modulo corrente, 
# quindi se sei in main.py il logger si chiamerà main.
logger = logging.getLogger(__name__)

#Funzione con decorator @app.get("/health") che definisce un endpoint GET /health.
# deve darti un messaggio nel terminale di tipo logger:
#2026-04-09 10:30:00 | INFO | main | Health check called
#mentre ritorna sull'endpoint {"status": "ok"}
@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}