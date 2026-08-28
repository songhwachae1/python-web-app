from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from python_web_app.core.security.jwt import TokenType, TokenClaims, verify_token
from python_web_app.config import get_settings

settings = get_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenClaims:
    claims = verify_token(token, settings.JWT_PUBLIC_KEY, TokenType.ACCESS)
    return claims