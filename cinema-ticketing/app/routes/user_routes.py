from fastapi import APIRouter, Depends, HTTPException
from app import schemas, models, security
from app.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = security.get_password_hash(user.password)
    new_user = models.User(username=user.username, email=user.email, password_hash=hashed_pw)
    db.add(new_user)
    db.commit()
    return {"msg": "User registered"}

@router.post("/login")
def login(login_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == login_data.username).first()
    if not user or not security.verify_password(login_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
