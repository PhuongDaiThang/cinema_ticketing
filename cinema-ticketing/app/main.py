from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user_routes, movie_routes, booking_routes,admin_routes
from app.middlewares import log_requests
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.middleware("http")(log_requests)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(admin_routes.router, prefix="/admin", tags=["Admin"])
app.include_router(movie_routes.router, prefix="/movies", tags=["Movies"])
app.include_router(booking_routes.router, prefix="/bookings", tags=["Bookings"])
