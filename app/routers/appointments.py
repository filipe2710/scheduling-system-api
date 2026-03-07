from fastapi import APIRouter, HTTPException, status

from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.services.scheduling_seruice import SchedulingService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

scheduling_service = SchedulingService()

@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED, summary="Create a new appointment", description="Create a new appointment after validating availability")
def create_appointment(appointment: AppointmentCreate):
  if not scheduling_service.validate_time_range(appointment):
    raise HTTPException(status_code=400, detail="Start time must be before end time")
 
  scheduling_service.create_appointment(appointment)
  
  return appointment

@router.get("/", response_model=list[AppointmentRead], status_code=status.HTTP_200_OK, summary="List all appointments", description="List all appointments")
def get_appointments():
  return scheduling_service.list_appointment()