from typing import List, Optional
from uuid import uuid4
from datetime import datetime

from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.core.enums import AppointmentStatus

class AppointmentService:
  """Service layer responsible for appointment-related business logic."""
  
  def __init__(self):
    self.appointments: List[AppointmentRead] = []
    
  def create_appointment(self, appointment: AppointmentCreate) -> AppointmentRead:
    """
    Create a new appointment.

    Args:
        appointment (AppointmentCreate): Input data for appointment creation.

    Returns:
        AppointmentRead: Created appointment with generated ID.
    """
    appointment_read = AppointmentRead(
      id=str(uuid4()),
      status=AppointmentStatus.pending,
      created_at=datetime.utcnow(),
      **appointment.model_dump()
    )
    
    self.appointments.append(appointment_read)
    return appointment_read
  