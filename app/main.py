
from fastapi import FastAPI

app = FastAPI(  # FastAPI == class main in framework
  title="scheduling system api",
  description="API for managing professional scheduling with conflict validation",
  version="1.0.0"
)

@app.get("/health") # decorator a reponse the request HTTP GET in path /health  (get: read, /health: check endpoint )
def health_check(): # funcion for check if the API is up and running
  return {"status": "ok"}