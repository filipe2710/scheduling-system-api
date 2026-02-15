from fastapi import FastAPI

# Application instance
# This file acts as the entry point of the API
app = FastAPI(
  title="scheduling system api",
  description="API for managing professional scheduling with conflict validation",
  version="1.0.0"
)

@app.get("/health") 
def health_check(): 
  """
  Health check endpoint.

  Used to verify if the application is running and responding.
  Commonly consumed by monitoring tools or during deployment.
  """
  return {"status": "ok"}