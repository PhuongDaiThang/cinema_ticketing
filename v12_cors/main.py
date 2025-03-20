from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # cho phép frontend này
    allow_credentials=True,
    allow_methods=["*"],                      # cho phép tất cả method: GET, POST, PUT...
    allow_headers=["*"],                      # cho phép tất cả header
)

@app.get("/")
def home():
    return {"message": "CORS configured"}
