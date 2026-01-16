from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import LoginRequest, Token
from app.services.users import authenticate_user
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login", response_model=Token)
def login(req: LoginRequest):
    user = authenticate_user(req.username, req.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    token = create_access_token(subject=user["username"], role=user["role"])
    return Token(access_token=token)
