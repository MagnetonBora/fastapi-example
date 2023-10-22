from dataclasses import dataclass

from fastapi import FastAPI


@dataclass
class UserInfo:
    email: str
    loging: str
    password: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/add_user")
async def add_user(info: UserInfo):
    return {"message": info}
