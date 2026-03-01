from passlib.context import CryptContext
#CryptContext → Used to hash & verify passwords
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "SUPER_SECRET_KEY_"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# This tells Use bcrypt algorithm to hash passwords.
#In passlib, deprecated refers to:
# Old hashing algorithms that should no longer be used for NEW passwords.

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)