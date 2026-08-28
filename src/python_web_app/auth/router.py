from typing import Annotated

from fastapi import APIRouter, Depends, Query, Body
from fastapi.security import OAuth2PasswordRequestForm

from python_web_app.auth.schema import RegisterRequest, RegisterResponse
from python_web_app.core.security.jwt import TokenPair
from python_web_app.auth.dependency import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])
"""
router = APIRouter(prefix="/auth", tags=["auth"], dependencies=[Depends(get_current_user)])
also possible to pass dependencies in a router.
The router dependencies are executed first, 
then the dependencies in the decorator, 
and then the normal parameter dependencies.
"""


@router.post("/register")
async def register(request: RegisterRequest):
    return RegisterResponse.model_validate(request)


"""
anything callable can be a dependency.
OAuth2PasswordRequestForm, here, is a class. 
a class is callable.
Annotated[OAuth2PasswordRequestForm, Depends()]
is the shortcut for 
Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]
"""
@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return TokenPair


"""
a path operation decorator receives an optional
argument dependencies. the value they return won't be passed
to the path operation function.
"""
@router.get("/me", dependencies=[Depends(get_current_user)])
async def me():
    return