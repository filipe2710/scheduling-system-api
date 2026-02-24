from fastapi import APIRouter

from app.schemas.client_create import ClientCreate
from app.services.client import ClientService

router = APIRouter(prefix="/clients", tags=["clients"])

client_service = ClientService()

@router.post("/")
def create_client(client: ClientCreate):
  """Create a new client"""
  
  client_service.create_client(client)
  
  return {
    "message": "client created successfully",
    "client": client,
  }
  
@router.get("/")
def get_clients():
  return client_service.list_client()