from pydantic import BaseModel
from datetime import date

class ClientRead(BaseModel):
  """Schema used to read a new client."""
  
  id: str
  name: str
  age: int
  phone: str
  date_of_birth: date
  cpf: str
  gender: str
  