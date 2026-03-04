from datetime import datetime
from pydantic import BaseModel
from uuid import UUID

class AppointmentCreate(BaseModel):
  """Schema used to create a new appointment."""
  
  client_id: UUID
  professional_id: UUID
  service_id: UUID
  start_time: datetime
  end_time: datetime
  