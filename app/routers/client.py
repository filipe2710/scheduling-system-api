from fastapi import APIRouter, status, HTTPException

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

@router.get("/{client_id}", response_model=Client_Read)
def get_client_by_id(client_id: str):
  client = client_service.get_client_by_id(client_id)
    
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client

@router.put("/{client_id}", response_model=Client_Read, status_code=status.HTTP_200_OK)
def put_client_by_id(client_id: str, item: ClientCreate):
  client = client_service.put_client_by_id(client_id, item)
  
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client

@router.delete("/{client_id}", response_model=Client_Read, status_code=status.HTTP_404_NOT_FOUND)
def delete_client_by_id(client_id: str):
  client = client_service.delete_client_by_id(client_id)
  
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client