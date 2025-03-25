from fastapi import Depends, HTTPException
from jose import jwt
from passlib.context import CryptContext
from datetime import timedelta, datetime
from sqlalchemy.orm import Session
from app.crud import get_user_by_username
from app.database import SessionLocal

SECRET_KEY = "secret"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(username: str):
    data = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(lambda: "FAKE"), db: Session = Depends(SessionLocal)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
        user = get_user_by_username(db, username)
        return user
    except:
        raise HTTPException(status_code=401)
