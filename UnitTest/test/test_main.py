import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest
from app.models import User
from app.main import app, get_db
from app.database import Base, SessionLocal, engine
from app.auth import get_current_user

# Tạo DB riêng cho test
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_register_success():
    response = client.post("/register", json={"username": "testuser", "password": "123"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_register_duplicate():
    client.post("/register", json={"username": "dupeuser", "password": "123"})
    response = client.post("/register", json={"username": "dupeuser", "password": "123"})
    assert response.status_code == 400

def test_login_success():
    client.post("/register", json={"username": "loginuser", "password": "123"})
    response = client.post("/login", json={"username": "loginuser", "password": "123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_fail():
    response = client.post("/login", json={"username": "wrong", "password": "123"})
    assert response.status_code == 401

def test_get_me():
    # Đăng ký + login
    client.post("/register", json={"username": "meuser", "password": "123"})
    res = client.post("/login", json={"username": "meuser", "password": "123"})
    token = res.json()["access_token"]

    # Override token (mock)
    def fake_get_current_user():
        db = next(override_get_db())
        return db.query(User).filter(User.username == "meuser").first()

    app.dependency_overrides[get_current_user] = fake_get_current_user

    response = client.get("/me")
    assert response.status_code == 200
    assert response.json()["username"] == "meuser"
