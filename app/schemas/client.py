from pydantic import BaseModel, field_validator
from datetime import date
from typing import Literal

class Clientcreate(BaseModel):
  """Schema used to create a new client."""
  
  name: str
  phone: str
  date_of_birth: date
  cpf: str
  gender: Literal["Masculino", "Feminino"]
  
  @field_validator("gender", mode="before")
  @classmethod
  def formalization_gender(self, gender: str) -> str:
    gender = gender.strip().lower().capitalize()