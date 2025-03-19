from fastapi import APIRouter, Depends
from app import models, schemas
from app.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@router.post("/")
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    new_movie = models.Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    return {"msg": "Movie created"}
