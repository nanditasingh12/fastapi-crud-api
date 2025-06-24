from fastapi.testclient import TestClient
from main import app  # replace with your FastAPI app module

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "The app is starting"}
