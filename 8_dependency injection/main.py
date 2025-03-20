from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency - logic chung
def get_token():
    return "my-secret-token"

# Endpoint sử dụng dependency
@app.get("/profile/")
def read_profile(token: str = Depends(get_token)):
    return {"token_used": token}
    
def verify_user(token: str = Depends(get_token)):
    if token != "my-secret-token":
        raise HTTPException(status_code=403, detail="Invalid token")
    return True

@app.get("/dashboard/")
def read_dashboard(auth: bool = Depends(verify_user)):
    return {"data": "Welcome to dashboard!"}
