from typing import List, Optional
from datetime import date
from uuid import uuid4

from app.schemas.client_create import ClientCreate
from app.schemas.client_read import ClientRead

class ClientService:
  """Service layer responsible for client-related business logic."""
  
  def __init__(self):
    self.clients: List[ClientRead] = []
    
  def create_client(self, client: ClientCreate) -> ClientRead:
    """
    Create a new client and calculate its age.

    Args:
        client (ClientCreate): Input data for client creation.

    Returns:
        ClientRead: Created client with generated ID and calculated age.
    """
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
    
  def list_client(self) -> List[ClientRead]:
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
    """
    Remove a customer based solely on identification.

    Args:
        client_id (str): The client's UUID

    Returns:
        bool: If client found return True else False
    """
    
    for index, client in enumerate(self.clients):
      if client_id == client.id:
        del self.clients[index]
        return True
    return 
  
  def put_client_by_id(self, client_id: str, item: ClientCreate) -> Optional[ClientRead]:
    """
    Updates all customer data by unique ID.

    Args:
        client_id (str): The client's UUID
        item (ClientCreate): Client creation

    Returns:
        Optional[ClientRead]: if found ID return ClientRead else False
    """
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
    """
    A protected method for calculating a client's age from their date of birth.
    
    Args:
        date_of_birth (date): date of birth in client

    Returns:
        int: always returns an integer
    """
    today = date.today()
    age = today.year - date_of_birth.year
    
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
      age -= 1
      
    return age
    