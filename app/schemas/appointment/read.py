from uuid import UUID
from datetime import datetime

from .base import AppointmentBase
from ...core.enums import AppointmentStatus

class AppointmentRead(AppointmentBase):
  id: UUID
  status: AppointmentStatus
  created_at: datetime