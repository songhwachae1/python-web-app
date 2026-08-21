from datetime import datetime, timedelta, timezone
from enum import StrEnum
from typing import Any
import uuid

import jwt
from pydantic import BaseModel

from python_web_app.config import get_settings

settings = get_settings()

ALG = settings.JWT_ALGORITHM
ISSUER = settings.JWT_ISSUER
AUDIENCE = settings.JWT_AUDIENCE
ACCESS_TOKEN_TTL = timedelta(minutes=settings.ACCESS_TOKEN_MTL)
REFRESH_TOKEN_TTL = timedelta(days=settings.REFRESH_TOKEN_DTL)
CLOCK_SKEW_LEEWAY = timedelta(days=settings.CLOCK_SKEW_LEEWAY)


class TokenPair:
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str #Bearer


class TokenClaims(BaseModel):
    sub: str
    role: str
    iat: int
    exp: int
    jti: str


class TokenType(StrEnum):
    ACCESS = "access"
    REFRESH = "refresh"


def _issue_token(
        private_key_pem: str,
        key_id: str,
        payload: dict[str, Any],
) -> str:
    headers = {
        "kid": key_id,
        "typ": "JWT"
    }

    return jwt.encode(payload, private_key_pem, algorithm=ALG, headers=headers)


def _build_token_payload(
        sub: str, 
        token_type: str,
        ttl: timedelta = ACCESS_TOKEN_TTL,
        role: str | None = None,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": sub,
        "iss": ISSUER,
        "aud": AUDIENCE,
        "iat": now,
        "exp": now + ttl,
        "jti": str(uuid.uuid4()),
        "type": token_type, # access/refresh
    }
    
    if role is not None:
        payload["role"] = role

    return payload

def issue_token_pair(
        sub: str, 
        role: str, 
        private_key_pem: str,
        key_id: str) -> TokenPair:
    access_token = _issue_token(
        private_key_pem, 
        key_id, 
        _build_token_payload(sub, TokenType.ACCESS, ACCESS_TOKEN_TTL, role)
    )

    refresh_token = _issue_token(
        private_key_pem, 
        key_id, 
        _build_token_payload(sub, TokenType.REFRESH, REFRESH_TOKEN_TTL)
    )

    return TokenPair(
        access_token=access_token, 
        refresh_token=refresh_token, 
        expires_in=ACCESS_TOKEN_TTL * 60, 
        token_type="Bearer"
    )
