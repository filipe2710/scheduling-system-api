from typing import List, Optional
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
  
  def get_client_by_id(self, client_id: str) -> Optional[Client_Read]:
    """
    Retrieve a client by its unique identifier.

    Args:
        client_id (str): The client's UUID.

    Returns:
        Client_Read | None: The client if found, otherwise None.
    """
    for client in self.clients:
      if client_id == client.id:
        return client
    return None
        
  def delete_client_by_id(self, client_id: str) -> bool:
    for index, client in enumerate(self.clients):
      if client_id == client.id:
        del self.clients[index]
        return True
    return 
  
  def put_client_by_id(self, client_id: str, item: ClientCreate) -> bool:
   for index, client in enumerate(self.clients):
     if client_id == client.id:
       updated_client = Client_Read(
        id=client.id,
        name=item.name,
        phone=item.phone,
        date_of_birth=item.date_of_birth,
        cpf=item.cpf,
        gender=item.gender,
        age=self._calculate_age(item.date_of_birth)
        )
       self.clients[index] = updated_client
       return True
   return False
        
  def _calculate_age(self, date_of_birth):
    pass
  