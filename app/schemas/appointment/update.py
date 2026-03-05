from pydantic import BaseModel
from datetime import datetime

from app.core.enums import AppointmentStatus

class AppointmentUpdate(BaseModel):
  start_at: datetime | None = None
  end_at: datetime | None = None
  status: AppointmentStatus | None = None