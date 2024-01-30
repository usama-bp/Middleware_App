# from starlette.requests import Request
# from starlette.responses import Response
# from ..models.model import Users_
# # from ..pydantic_model import s
# from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials,OAuth2PasswordBearer
# from jose import jwt, JWTError
# from fastapi import Depends,HTTPException
# import secrets
# import string
# from datetime import timedelta,datetime
# from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint




# SECRET_KEY='ff2be0777c49a5fd93de4bec9c6eb72a'
# ALGORITHM="HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES=30

# auth_scheme=HTTPBearer()



# async def checkuser(request:Request):
#     try:
#          data=await request.json()
#          name=data.get("name")
#          password=data.get("password")
#          username=data.get("username")

#          users=await Users_.get(name=name,password=password)
#          if users:
#             passed=await users.check_pass(password)
#             if passed:
#                 return True
#             else:
#                 return{"message":"Wrong Password"}
#          else:
#             return {"message":"Users DoesNOtExist"}
#     except Exception as e:
#            return {"message":f"{e}"}
             
    

