from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Model cho dữ liệu trả về
class UserResponse(BaseModel):
    id: int
    name: str
    message: str

# Endpoint với response model + status code
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user():
    return {"id": 1, "name": "Alice", "message": "User created successfully"}
