import logging
from fastapi import FastAPI
from routers.tasks_base import router as tasks_base_router

app = FastAPI()
app.include_router(tasks_base_router)

from middleware import setup_logging_middleware
setup_logging_middleware(app)


# mostra i messaggi di livello INFO o superiore (esclude i DEBUG)
# il formato di ogni riga di log: 
# %(asctime)s  è il timestamp, 
# %(levelname)s → livello tipo info, warning, error o altro.
# %(name)s → nome di chi logga (non sono sicuro di capire cosa faccia)
# %(message)s il messaggio che scrivi tu in questo caso dato dal decorator 
#datefmt="%Y-%m-%d %H:%M:%S" è il formato del timestamp (2026-04-09 10:30:00)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
#logger = logging.getLogger(__name__) — crea un logger specifico per questo file
#__name__ è una variabile Python che vale il nome del modulo corrente, 
# quindi se sei in main.py il logger si chiamerà main.
logger = logging.getLogger(__name__)


#idealmente deve darti un messaggio nel terminale di tipo logger:
#2026-04-09 10:30:00 | INFO | main | Health check called
#questo può farlo perché metto un decorator che dice che quando
#viene chiamato l'endpoint /health, esegui la funzione health_check()
#cioè richiama in logger.info il messaggio "Health check called"
#Mentre nell'endpoint ritorna un dizionario con "status": "ok"
@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok"}