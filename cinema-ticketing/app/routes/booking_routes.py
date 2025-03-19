from fastapi import APIRouter, Depends
from app import models, schemas
from app.dependencies import get_db, get_current_user
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/")
def book_ticket(booking: schemas.BookingCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ticket = models.Ticket(
        showtime_id=booking.showtime_id,
        seat_number=booking.seat_number,
        user_id=user.id,
        price=booking.price
    )
    db.add(ticket)
    db.commit()
    return {"msg": "Booking successful"}

@router.get("/history")
def booking_history(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(models.Ticket).filter(models.Ticket.user_id == user.id).all()
