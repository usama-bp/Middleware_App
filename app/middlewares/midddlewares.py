from fastapi import  HTTPException
from dotenv import load_dotenv
import os
from..pydantic_model.schemaModel import User_s
from ..security.auth import create_access_token,authenticate_user,create_refresh_token,authenticate_user
from datetime import timedelta


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS =int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS")) 






async def login_middle(user:User_s):
     users=await authenticate_user(user.username,user.password)
     if not users:
          raise HTTPException(status_code=404,detail="NotFound")
     refresh_time=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
     access_time=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     access_token=create_access_token(data={"sub":user.username},expires_delta=access_time)
     refresh_token=await create_refresh_token(data={"sub":user.username},expires_delta=refresh_time)
     result={
         "access_token":access_token,
         "refresh_token":refresh_token,
         "token_type":"bearer",
     }
     return result



