from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET endpoint
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

# Định nghĩa schema cho dữ liệu gửi lên từ client
class UserRequest(BaseModel):
    name: str

# POST endpoint
@app.post("/greet")
def greet_user(user: UserRequest):
    return {"message": f"Hello {user.name}!"}
