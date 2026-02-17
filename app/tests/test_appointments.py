from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_creat_appointment_with_invalid_time():
  """Should return 400 when start_time is greater time or equal to end_time"""

  payload = {
    
    "user_id": 1,
    "professional_id": 1,
    "start_time": "2026-02-16T10:00:00",
    "end_time": "2020-02-16T09:00:00"
  }

  response = client.post("/appointments", json=payload)

  assert response.status_code == 400