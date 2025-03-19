from sqlalchemy.orm import Session
from app import models, schemas

# CRUD MOVIE
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_all_movies(db: Session):
    return db.query(models.Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def delete_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie

# CRUD SHOWTIME
def create_showtime(db: Session, showtime: schemas.ShowtimeCreate):
    db_showtime = models.Showtime(**showtime.dict())
    db.add(db_showtime)
    db.commit()
    db.refresh(db_showtime)
    return db_showtime

def get_all_showtimes(db: Session):
    return db.query(models.Showtime).all()
