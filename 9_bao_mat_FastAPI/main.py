from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "secret"
ALGORITHM = "HS256"

# Fake DB user
fake_user = {"username": "alice", "password": "secret"}

# Login để cấp token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != fake_user["username"] or form_data.password != fake_user["password"]:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    token_data = {"sub": form_data.username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

# API bảo vệ
@app.get("/protected/")
def protected_route(token_data: dict = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token_data, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Access granted", "user": payload}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")