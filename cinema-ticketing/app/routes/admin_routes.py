from fastapi import APIRouter, Depends, HTTPException
from app import crud, schemas, models
from app.dependencies import get_db, get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

# Middleware kiểm tra quyền admin
def admin_required(current_user=Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")
    return current_user

# --- CRUD PHIM ---

@router.post("/movies")
def admin_create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), _: models.User = Depends(admin_required)):
    return crud.create_movie(db, movie)

@router.delete("/movies/{movie_id}")
def admin_delete_movie(movie_id: int, db: Session = Depends(get_db), _: models.User = Depends(admin_required)):
    movie = crud.delete_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"msg": "Movie deleted"}

# --- CRUD SHOWTIME ---

@router.post("/showtimes")
def admin_create_showtime(showtime: schemas.ShowtimeCreate, db: Session = Depends(get_db), _: models.User = Depends(admin_required)):
    return crud.create_showtime(db, showtime)

@router.get("/showtimes")
def admin_list_showtimes(db: Session = Depends(get_db), _: models.User = Depends(admin_required)):
    return crud.get_all_showtimes(db)
