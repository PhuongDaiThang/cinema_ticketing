from fastapi import FastAPI, Request,BackgroundTasks,Form

app = FastAPI()


def send_email(email: str):
    print(f"Sending email to {email}")

@app.post("/notify/")
def notify_user(background_tasks: BackgroundTasks, email: str = Form(...)):
    background_tasks.add_task(send_email, email)
    return {"message": "Notification scheduled"}

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    print(f"Incoming request: {request.url}")
    response = await call_next(request)
    print("Request processed")
    return response
