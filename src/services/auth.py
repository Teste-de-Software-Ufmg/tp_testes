from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

from src.config import envs



SECRET_KEY = envs.base_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Create a JSON Web Token (JWT) for the given data with an optional expiration time.

    Args:
        data (dict): The data to encode in the JWT.
        expires_delta (timedelta | None, optional): The time duration after which the token will expire. 
            If not provided, a default expiration time will be used.

    Returns:
        str: The encoded JWT as a string.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    """
    Verifies the provided JWT token.

    Args:
        token (str): The JWT token to be verified.

    Returns:
        dict: The decoded payload of the token if verification is successful.

    Raises:
        HTTPException: If the token is invalid or expired, an HTTP 401 Unauthorized exception is raised.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as exc:
        raise HTTPException(
            status_code=401, 
            detail="Invalid or expired token"
        ) from exc

def get_current_user(token: str = Depends(OAUTH2_SCHEME)):
    """
    Retrieve the current user based on the provided OAuth2 token.

    Args:
        token (str): The OAuth2 token used for authentication.

    Returns:
        dict: The payload containing user information extracted from the token.
    """
    payload = verify_token(token)
    return payload