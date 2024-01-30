from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from ..pydantic_model.schemaModel import User_s,Token,TokenData
from ..models.model import Users_
import os
from dotenv import load_dotenv



load_dotenv()

# to get a string like this run:
# openssl rand -hex 32



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")














oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()








async def get_user(username: str):
    user = await Users_.get(username=username)
    print(user)
    return user


async def authenticate_user(username: str, password: str):
    user = await Users_.get(username=username)
    if not user:
        return False
    if not await user.check_pass(password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = Users_.get(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


# async def get_current_active_user(
#     current_user: Annotated[str, Depends(get_current_user)]
# ):
#     if not current_user:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @


# @app.get("/users/me/", response_model=User_s)
# async def read_users_me(
#     current_user: Annotated[User_s, Depends(get_current_active_user)]
# ):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(
#     current_user: Annotated[User_s, Depends(get_current_active_user)]
# ):
#     return [{"item_id": "Foo", "owner": current_user.username}]