from typing import List
from app.schemas.client import ClientCreate

class ClientService:
  """Class control services of clients"""
  
  def __init__(self):
    self.clients: List[ClientCreate] = []
    
  def create_client(self, client: ClientCreate):
    self.clients.append(client)
    
  def list_client(self):
    return self.clients