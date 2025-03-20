from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Tạo model với Pydantic
class User(BaseModel):
    name: str
    age: int
    email: str

# Sử dụng model trong endpoint POST
@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} created!", "data": user}
