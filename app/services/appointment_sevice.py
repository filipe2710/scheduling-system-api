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
  
  def validate_availability(self, new_appointment: AppointmentCreate) -> bool:
    """ 
    validates if a professional is available for the given time slot. 
    
    args:
      new_appointment (AppointmentCreate): The appointment to check for availability.
      
    Returns:
      bool: True if the professional is available, False otherwise.
    """
    
    for appointment in self.appointments:
      if appointment.professional_id != new_appointment.professional_id:
        continue
      
      if (new_appointment.start_time < appointment.end_time and new_appointment.end_time > appointment.start_time):
        return False
      
    return True
  
  def validate_time_range(self, appointment: AppointmentCreate) -> bool:
    """
    Ensures start time is before end time.
    
    Args:
      appointment (AppointmentCreate): The appointment to validate.

    Returns:
      bool: True if the time range is valid, False otherwise.
    """

    if appointment.start_time >= appointment.end_time:
      return False
    return True
  
  def create_appointment(self, appointment: AppointmentCreate):   
    self.appointments.append(appointment)
    
  def list_appointment(self):
    return self.appointments
  