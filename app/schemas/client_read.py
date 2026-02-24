from pydantic import BaseModel
from datetime import date

class Client_Read(BaseModel):
  id: str
  name: str
  age: str
  phone: str
  date_of_birth: date
  cpf: str
  gender: str
  