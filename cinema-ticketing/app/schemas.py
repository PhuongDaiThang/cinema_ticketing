from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class MovieCreate(BaseModel):
    title: str
    description: str
    duration: int
    poster_url: str
    trailer_url: str

class ShowtimeCreate(BaseModel):
    movie_id: int
    room: str
    show_date: str
    show_time: str

class BookingCreate(BaseModel):
    showtime_id: int
    seat_number: str
    price: float
