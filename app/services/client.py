from typing import List, Optional
from datetime import date
from uuid import uuid4

from app.schemas.client_create import ClientCreate
from app.schemas.client_read import ClientRead

class ClientService:
  """Class control services of clients"""
  
  def __init__(self):
    self.clients: List[ClientRead] = []
    
  def create_client(self, client: ClientCreate) -> ClientRead:
    client_read = ClientRead(
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
    
  def list_client(self) -> list[ClientRead]:
    return self.clients
  
  def get_client_by_id(self, client_id: str) -> Optional[ClientRead]:
    """
    Retrieve a client by its unique identifier.

    Args:
        client_id (str): The client's UUID.

    Returns:
        ClientRead | None: The client if found, otherwise None.
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
  
  def put_client_by_id(self, client_id: str, item: ClientCreate) -> Optional[ClientRead]:
   for index, client in enumerate(self.clients):
     if client_id == client.id:
       updated_client = ClientRead(
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
        
  def _calculate_age(self, date_of_birth: date) -> int:
    today = date.today()
    age = today.year - date_of_birth.year
    
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
      age -= 1
      
    return age
    