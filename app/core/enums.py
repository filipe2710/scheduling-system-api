from enum import Enum

class AppointmentStatus(str, Enum):
  draft = "Draft"
  pending = "Pending"
  confirmed = "Confirmed"
  in_progress = "In Progress"
  completed = "Completed"
  postponed = "Postponed"
  canceled = "Canceled"