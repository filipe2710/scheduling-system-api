from fastapi import APIRouter, HTTPException

from app.schemas.appointment import Appointmentcreate
from app.services.scheduling_seruice import SchedulingService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

scheduling_service = SchedulingService()

@router.post("/")
def create_appointment(appointment: Appointmentcreate):
  """Create a new appointment after validating availability"""
    
  if not scheduling_service.validate_time_range(appointment):
    raise HTTPException(status_code=400, detail="Start time must be before end time")
 
  scheduling_service.create_appointment(appointment)
  
  return {
    "message": "appointment created successfully",
    "appointment": appointment,
  }
  
@router.get("/")
def get_appointments():
  return scheduling_service.list_appointment()