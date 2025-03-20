from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from v10_connect_database.user import User

app = FastAPI()

@app.get("/users/")
async def get_users():
    return await User.all()

register_tortoise(
    app,
    db_url="mysql://root:1234@localhost:3306/mydb",
    modules={"models": ["v10_connect_database.user"]}, 
    generate_schemas=True,
    add_exception_handlers=True,
)
