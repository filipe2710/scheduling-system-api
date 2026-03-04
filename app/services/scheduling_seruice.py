from typing import List
from app.schemas.appointment import AppointmentCreate

class SchedulingService:
  """Service responsible for scheduling business rules"""
  
  def __init__(self):
    self.appointments: List[AppointmentCreate] = []
  
  def validate_availability(self, new_appointment: AppointmentCreate) -> bool:
    """ validates if a professional is available for the given time slot. """
    
    for appointment in self.appointments:
      if appointment.professional_id != new_appointment.professional_id:
        continue
      
      if (new_appointment.start_time < appointment.end_time and new_appointment.end_time > appointment.start_time):
        return False
      
    return True
  
  def validate_time_range(self, appointment):
    """Ensures start time is before end time."""
    if appointment.start_time >= appointment.end_time:
      return False
    return True
  
  def create_appointment(self, appointment: AppointmentCreate):   
    self.appointments.append(appointment)
    
  def list_appointment(self):
    return self.appointments
  