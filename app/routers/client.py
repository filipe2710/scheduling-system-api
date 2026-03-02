from fastapi import APIRouter, status, HTTPException

from app.schemas.client_create import ClientCreate
from app.schemas.client_read import ClientRead
from app.services.client import ClientService

router = APIRouter(prefix="/clients", tags=["clients"])

client_service = ClientService()

@router.post("/", response_model=ClientRead, status_code=status.HTTP_201_CREATED, summary="Create a new client", description="Creates a new client and automatically calculates the age based on date_of_birth.")
def create_client(client: ClientCreate):
  new_client = client_service.create_client(client)
  
  return new_client
  
@router.get("/", response_model=list[ClientRead], status_code=status.HTTP_200_OK, summary="List all clients", description="List all clients")                           
def get_clients():
  return client_service.list_client()

@router.get("/{client_id}", response_model=ClientRead, status_code=status.HTTP_200_OK, summary="Get client by ID", description="Get client by ID. Return 404 if not found")
def get_client_by_id(client_id: str):
  client = client_service.get_client_by_id(client_id)
    
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client

@router.put("/{client_id}", response_model=ClientRead, status_code=status.HTTP_200_OK, summary="Update a client by ID", description="Update a client by ID. Return 404 if not found")
def put_client_by_id(client_id: str, item: ClientCreate):
  client = client_service.put_client_by_id(client_id, item)
  
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client

@router.delete("/{client_id}", response_model=ClientRead, status_code=status.HTTP_404_NOT_FOUND, summary="Delete a client by ID", description="Delete a client by ID. Returns the deleted client.")
def delete_client_by_id(client_id: str):
  client = client_service.delete_client_by_id(client_id)
  
  if client is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client not found")
  
  return client