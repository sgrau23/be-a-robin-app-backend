from passlib.context import CryptContext
from jose import jwt
from src.utils import get_settings
from datetime import datetime, timedelta

# Load settings
SETTINGS = get_settings('crypto')

# Initialize context to hash passwords
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password):
    return password_context.hash(password)


def verify_password(password, hashed_pass):
    return password_context.verify(password, hashed_pass)


def create_access_token(subject, expires_delta=None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            minutes=SETTINGS['access_token_expire_minutes']
        )
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SETTINGS['secret_key'], SETTINGS['algorithm'])
    return encoded_jwt


def create_refresh_token(subject, expires_delta=None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(
            days=SETTINGS['refresh_token_expire_days']
        )
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SETTINGS['refresh_secret_key'], SETTINGS['algorithm'])
    return encoded_jwt


def get_access_tokens(email):
    return {
        "access_token": create_access_token(email),
        "refresh_token": create_refresh_token(email),
    }
