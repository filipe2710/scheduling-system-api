from typing import List
from pydantic import Field
from uuid import uuid4
from app.schemas.client_create import ClientCreate
from app.schemas.client_read import Client_Read

class ClientService:
  """Class control services of clients"""
  
  def __init__(self):
    self.clients: List[Client_Read] = []
    
  def create_client(self, client: ClientCreate) -> Client_Read:
    client_read = Client_Read(
      id=str(uuid4()),
      name=client.name,
      phone=client.phone,
      date_of_birth=client.date_of_birth,
      cpf=client.cpf,
      gender=client.gender,
      age=self._calculate_age(client.date_of_birth)
    )
    
    self.clients.append(client_read)
    return client_read
    
  def list_client(self) -> list[Client_Read]:
    return self.clients
  
  def _calculate_age(self, date_of_birth):
    pass
  