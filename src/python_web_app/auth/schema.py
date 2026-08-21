from pydantic import BaseModel

from python_web_app.common.schema import SnakeModel


class RegisterRequest(BaseModel):
    email: str
    password: str
    fname: str
    lname: str


class RegisterResponse(SnakeModel):
    email: str
    fname: str
    lname: str