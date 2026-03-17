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
  
  def get_appointment_by_id(self, appointment_id: str) -> Optional[AppointmentRead]:
    """
    Retrieve an appointment by its unique identifier.

    Args:
        appointment_id (str): The appointment's UUID.

    Returns:
        AppointmentRead | None: The appointment if found, otherwise None.
    """
    for appointment in self.appointments:
      if appointment_id == appointment.id:
        return appointment
    return None
  
  def put_appointment_by_id(self, appointment_id: str, appointment_update: AppointmentUpdate) -> Optional[AppointmentRead]:
    """
    Update an existing appointment.

    Args:
        appointment_id (str): The appointment's UUID.
        appointment_update (AppointmentUpdate): The updated appointment data.

    Returns:
        AppointmentRead | None: The updated appointment if found, otherwise None.
    """
    for index, appointment in enumerate(self.appointments):
      
      if appointment_id == appointment.id:
        update_data = appointment_update.model_dump(exclude_unset=True)
        
        if "status" in update_data:
          new_status = update_data["status"]
          
          if not self._validate_status_transition(appointment.status, new_status):
            raise ValueError(f"Invalid status transition from {appointment.status} to {new_status}")
          
        updated_appointment = appointment.model_copy(update=update_data)
        self.appointments[index] = updated_appointment
        return updated_appointment
    return 
  
  def _validate_status_transition(self, current_status: AppointmentStatus, new_status: AppointmentStatus) -> bool:
    """
    Validates if the status transition is allowed based on predefined rules.

    Args:
        current_status (AppointmentStatus): The current status of the appointment.
        new_status (AppointmentStatus): The new status to transition to.
        
    Returns:
        bool: True if the transition is valid, False otherwise.
    """
    valid_transitions = {
      AppointmentStatus.draft: [AppointmentStatus.pending],
      AppointmentStatus.pending: [AppointmentStatus.confirmed, AppointmentStatus.changed, AppointmentStatus.postponed],
      AppointmentStatus.confirmed: [AppointmentStatus.in_progress, AppointmentStatus.postponed, AppointmentStatus.changed],
      AppointmentStatus.in_progress: [AppointmentStatus.completed, AppointmentStatus.postponed],
      AppointmentStatus.postponed: [AppointmentStatus.confirmed, AppointmentStatus.changed],
      AppointmentStatus.completed: [],
      AppointmentStatus.changed: [AppointmentStatus.confirmed, AppointmentStatus.postponed]
    }
    
    if current_status == new_status:
      return True
    
    allowed_statuses = valid_transitions.get(current_status, [])
    
    return new_status in allowed_statuses
        
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
  
  def list_appointment(self):
    return self.appointments
  