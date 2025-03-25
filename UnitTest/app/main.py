from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from app.database import SessionLocal, engine, Base
from app import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_pw = get_password_hash(user.password)
    return crud.create_user(db, user.username, hashed_pw)

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_access_token(db_user.username), "token_type": "bearer"}

@app.get("/me", response_model=schemas.UserOut)
def read_users_me(current_user: schemas.UserOut = Depends(get_current_user)):
    return current_user
