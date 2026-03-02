from fastapi import APIRouter, HTTPException, status

from app.schemas.appointment import AppointmentCreate
from app.services.scheduling_seruice import SchedulingService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

scheduling_service = SchedulingService()

@router.post("/", response_model=AppointmentCreate, status_code=status.HTTP_201_CREATED, summary="Create a new appointment", description="Create a new appointment after validating availability")
def create_appointment(appointment: AppointmentCreate):
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