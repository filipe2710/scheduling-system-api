from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class AppointmentBase(BaseModel):
  
  client_id: UUID
  professional_id: UUID
  service_id: UUID
  start_time: datetime
  end_time: datetime
  