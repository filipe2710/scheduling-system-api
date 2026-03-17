from fastapi import APIRouter, HTTPException, status

from app.schemas.appointment import AppointmentCreate, AppointmentRead, AppointmentUpdate
from app.services.appointment_sevice import AppointmentService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

appointment_service = AppointmentService()

@router.post("/", response_model=AppointmentRead, status_code=status.HTTP_201_CREATED, summary="Create a new appointment", description="Create a new appointment after validating availability")
def create_appointment(appointment: AppointmentCreate):
  if not appointment_service.validate_time_range(appointment):
    raise HTTPException(status_code=400, detail="Start time must be before end time")
 
  appointment_service.create_appointment(appointment)
  
  return appointment

@router.get("/", response_model=list[AppointmentRead], status_code=status.HTTP_200_OK, summary="List all appointments", description="List all appointments")
def get_appointments():
  return appointment_service.list_appointment()

@router.get("/{appointment_id}", response_model=AppointmentRead, status_code=status.HTTP_200_OK, summary="Get appointment by ID", description="Get appointment by ID. Return 404 if not found")
def get_appointment_by_id(appointment_id: str):
  appointment = appointment_service.get_appointment_by_id(appointment_id)
  
  if appointment is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
  
  return appointment