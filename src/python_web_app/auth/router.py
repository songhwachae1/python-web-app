from typing import Annotated

from fastapi import APIRouter, Query, Body

from python_web_app.auth.schema import RegisterRequest, RegisterResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
async def register(request: RegisterRequest):
    return RegisterResponse.model_validate(request)
