from fastapi import FastAPI

from app.routers import appointments, client

# Application instance
# This file acts as the entry point of the API
app = FastAPI(
  title="scheduling system api",
  description="API for managing professional scheduling with conflict validation",
  version="1.0.0"
)

app.include_router(appointments.router)
app.include_router(client.router)

@app.get("/health") 
def health_check(): 
  """Health check endpoint by monitoring tools."""
  return {"status": "ok"}