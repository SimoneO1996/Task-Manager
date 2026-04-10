import time, logging
from fastapi import FastAPI, Request


#Dice a FastAPI: "questa funzione qui sotto intercetta tutte le richieste HTTP".
# È un decorator, come @app.get("/health") 
# ma invece di un endpoint registra un middleware.

def setup_logging_middleware(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        
#La funzione che viene eseguita ad ogni richiesta. Riceve due argomenti: 
#1) request la richiesta in arrivo 
#2) call_next la funzione che passa la richiesta all'endpoint

        logger = logging.getLogger("http")
        start = time.time() #Segna il momento in cui arriva la richiesta (s)
        logger.info(f"→ {request.method} {request.url.path}") #Logga l'ingresso, es. → GET /health
        #Qui il middleware si ferma e lascia che l'endpoint finisca.
        #Quando ha finito, la risposta è salvata in response.
        response = await call_next(request) 
        ms = round((time.time() - start) * 1000, 2) #calcolo tempo impiegato
        logger.info(f"← {response.status_code} {request.url.path} [{ms}ms]") #riscrive nel log l'uscita 
        return response #return nella funzione middleware la response