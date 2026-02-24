from pydantic import BaseModel, field_validator
from datetime import date
from typing import Literal
import re

class ClientCreate(BaseModel):
  """Schema used to create a new client."""
  
  name: str
  phone: str
  date_of_birth: date
  cpf: str
  gender: Literal["Masculino", "Feminino"]
  
  @field_validator("gender", mode="before")
  @classmethod
  def formalization_gender(cls, value: str) -> str:
    value = value.strip().lower().capitalize()
    
    if value not in ("Masculino", "Feminino"):
      raise ValueError("gender must be Masculino or Feminino")
    
    return value
  
  @field_validator("phone", mode="before")
  @classmethod
  def formalization_phone(cls, value: str) -> str:
    phone = re.sub(r"\D", "", value)
    
    if len(phone) not in (10, 11):
      raise ValueError("phone must have 10 or 11 digits")
    
    return phone
  
  @field_validator("cpf", mode="before")
  @classmethod
  def formalize_cpf(cls, value: str) -> str:
    cpf = re.sub(r"\D", "", value)
    
    if len(cpf) != 11:
      raise ValueError("cpf must have 11 digits")
    
    return cpf