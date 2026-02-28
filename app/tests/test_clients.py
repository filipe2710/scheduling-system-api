from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_client():
  response = client.post(
    "/clients/",
    json={
      "name": "Filipe",
      "phone": "11999999999",
      "date_of_birth": "2005-02-03",
      "cpf": "12345678901",
      "gender": "Masculino"
    }
  )
  assert response.status_code == 201
  
  body = response.json()
  assert body["name"] == "Filipe"
  assert body["gender"] == "Masculino"
  assert "id" in body
  
def test_list_clients():
  response = client.get("/clients/")
  assert response.status_code == 200
  assert isinstance(response.json(), list)
  
def test_get_client_not_found():
  response = client.get("/clients/invalid-id")
  assert response.status_code == 404
  
def test_delete_client_not_found():
  response = client.delete("/clients/invalid-id")
  assert response.status_code == 404