# backend/app/auth.py

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# JWT Config
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretchangeinprod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

# Admin credentials
ADMIN_USERNAME = os.getenv("ADMIN_USER", "admin")

# Get password, LIMIT to 72 chars
raw_admin_pass = os.getenv("ADMIN_PASS", "adminpass")
raw_admin_pass = raw_admin_pass[:72]

# Hash it safely
ADMIN_PASSWORD_HASH = pwd_context.hash(raw_admin_pass)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_admin(username: str, password: str):
    if username != ADMIN_USERNAME:
        return False
    if not verify_password(password, ADMIN_PASSWORD_HASH):
        return False
    return {"username": username}


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_admin(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username != ADMIN_USERNAME:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
