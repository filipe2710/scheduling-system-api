from enum import Enum

class AppointmentStatus(str, Enum):
  draft = "Draft"
  pending = "Pending"
  confirmed = "Confirmed"
  changed = "Changed"
  in_progress = "In Progress"
  completed = "Completed"
  postponed = "Postponed"
  canceled = "Canceled"