from fastapi import APIRouter, status

from app.schemas.client_create import ClientCreate
from app.schemas.client_read import Client_Read
from app.services.client import ClientService

router = APIRouter(prefix="/clients", tags=["clients"])

client_service = ClientService()

@router.post("/", response_model=Client_Read, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate):
  """Create a new client"""
  
  client_service.create_client(client)
  
  
@router.get("/", response_model=list[Client_Read])
def get_clients():
  return client_service.list_client()