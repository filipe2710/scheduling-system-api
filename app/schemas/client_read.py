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
  
  class Config:
      json_schema_extra = {
          "example": {
              "id": "uuid-string",
              "name": "Filipe",
              "age": 21,
              "phone": "11999999999",
              "date_of_birth": "2005-02-03",
              "cpf": "12345678901",
              "gender": "Masculino"
          }
      }