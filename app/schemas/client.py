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
  def formalization_gender(self, gender: str) -> str:
    gender = gender.strip().lower().capitalize()
  
  @field_validator("phone", mode="before")
  @classmethod
  def formalization_phone(self, phone: str) -> str:
    phone = re.sub(r"\b", "", phone)
    
    if len(phone) not in (10, 11):
      raise ValueError("phone must have 10 or 11 digits")
    
    return phone
  
  @field_validator("phone", mode="before")
  @classmethod
  def formalize_cpf(cls, cpf: str) -> str:
    cpf = re.sub(r"\D", "", cpf)
    
    if len(cpf) != 11:
      raise ValueError("cpf must have 11 digits")
    
    return cpf