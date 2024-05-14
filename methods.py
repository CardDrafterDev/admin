from jose import JWTError, jwt
from passlib.context import CryptContext
import datetime

import os, dotenv # for env


from fastapi import Response


dotenv.load_dotenv()

SECRET_KEY = os.environ["JWT_SECRET"]
ALGORITHM = os.environ["ALGO"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["TOKEN_EXP"])

# Sample admin user for now
def get_admin_user() -> dict[str, str]:
    admin_user = {
        "username": os.environ["ADMIN_USER"],
        "password": os.environ["ADMIN_PSWD"] # hashed password for "admin"
    }

    return admin_user


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_in: datetime.timedelta = 15) -> str:
    to_encode = data.copy()

    now = datetime.datetime.now(datetime.timezone.utc)

    if expires_in:
        expire = now + datetime.timedelta(minutes=expires_in)
    else:
        expire = now + datetime.timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def decode_token(token: str) -> dict[str, any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except JWTError as e:
        raise JWTError


# setting a cookie with exp and jwt into fastapi Response
def set_cookie(response: Response, jwt_token: str, expires_in: datetime.timedelta) -> None:
    exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=expires_in)
    response.set_cookie(key="jwt-token", value=jwt_token, httponly=True, expires=exp, secure=True)
    response.set_cookie(key="token-exp", value=exp, secure=True)
