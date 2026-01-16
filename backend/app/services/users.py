"""A minimal in-memory user store for MVP.

Replace with real user table + SSO later.
"""

from app.core.security import get_password_hash, verify_password


# demo users
_USERS = {
    "admin": {"username": "admin", "role": "admin", "password_hash": get_password_hash("admin123")},
    "dev": {"username": "dev", "role": "member", "password_hash": get_password_hash("dev123")},
}


def authenticate_user(username: str, password: str):
    user = _USERS.get(username)
    if not user:
        return None
    if not verify_password(password, user["password_hash"]):
        return None
    return {"username": user["username"], "role": user["role"]}
