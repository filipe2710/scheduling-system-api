from datetime import datetime
from pydantic import BaseModel

class Appointmentcreate(BaseModel):
  """Schema used to create a new appointment."""
  
  user_id: int
  professional_id: int
  start_time: datetime
  end_time: datetime