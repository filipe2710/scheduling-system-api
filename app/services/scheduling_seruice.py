from typing import List
from app.schemas.appointment import Appointmentcreate

class SchedulingService:
  """Service responsible for scheduling business rules"""
  
  def __init__(self):
    self.appointments: List[Appointmentcreate] = []
  
  def validate_availability(self, new_appointment: Appointmentcreate) -> bool:
    """ validates if a professional is available for the given time slot. """
    
    for appointment in self.appointments:
      if appointment.professional_id != new_appointment.professional_id:
        continue
      
      if (new_appointment.start_time < appointment.end_time and new_appointment.end_time > appointment.start_time):
        return False
      
    return True
  
  def create_appointment(self, appointment: Appointmentcreate):
    """Stores the appointment in memory"""
    
    self.appointments.append(appointment)