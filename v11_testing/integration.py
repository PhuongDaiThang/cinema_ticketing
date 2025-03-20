from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
fake_db = []

@app.post("/users/")
def create_user(name: str):
    fake_db.append(name)
    return {"user": name}

client = TestClient(app)

def test_create_user():
    response = client.post("/users/?name=Alice")
    assert response.status_code == 200
    assert response.json() == {"user": "Alice"}
    assert "Alice" in fake_db
