from fastapi import APIRouter, HTTPException

from app.schemas.appointment import Appointmentcreate
from app.services.scheduling_seruice import SchedulingService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

scheduling_service = SchedulingService()

@router.post("/")
def create_appointment(appointment: Appointmentcreate):
  """Create a new appointment after validating availability"""
  
  is_available = scheduling_service.validate_availability(appointment)
  
  if not is_available:
    raise HTTPException(status_code=400, detail="time slot not avaiable")
  
  return {
    "message": "appointment created successfully",
    "appointment": appointment,
  }