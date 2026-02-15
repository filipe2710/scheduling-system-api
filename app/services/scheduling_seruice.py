
class SchedulingService:
  """Service responsible for scheduling business rules"""
  
  def validate_availability(self, appointment_data):
    """ validates if a professional is available for the given time slot.

        for now, this method always returns True
    """
    return True