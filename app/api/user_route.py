from fastapi import APIRouter,Depends
from ..models.model import Users_
from tortoise.contrib.pydantic import pydantic_model_creator
from ..pydantic_model.schemaModel import User_s,savepassword
from fastapi.requests import Request
from typing import Annotated
from ..api.user_route import *
from ..middlewares.midddlewares import login_middle


import os
from dotenv import load_dotenv



load_dotenv()


pydanticuser=pydantic_model_creator(Users_)

routes = APIRouter()



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAY=int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))






     



@routes.get("/")
async def get_users(request:Request):
        allusers=await Users_.all()
        for user in allusers:
             orderd=[{
             "id": user.id,
            "name": user.name,
            "username": user.username,
            "password": user.password
         }]
        print(request.headers)
        
        return allusers
@routes.post("/addusers/")
async def create_user(users:User_s):
    try:
        password= users.password
        user=await Users_.create(username=users.username,name=users.name,password=savepassword(password))
        return {"message":"user created"}
    except Exception as e:
        return {"message":str(e)}


@routes.get("/getuser/{id}")
async def get_user(id:int):
    user=await Users_.get(id=id)
    return user

@routes.put("/updateuser/{id}")
async def update(id:int,users:User_s):
    user=await Users_.get(id=id)
    user.name=users.name
    user.username=users.username
    user.password=savepassword(users.password)
    await user.save()
    return {"message":"user updated"}

@routes.delete("/deleteuser/{id}")
async def delete(id:int):
    user=await Users_.get(id=id)
    await user.delete()
    return {"message":"user deleted"}


@routes.post("/login")
async def login(user:Annotated[dict,Depends(login_middle)]):

    if not user:
         return user
         

    return user




















# async def login_for_access_token(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
# ) -> Token:
#     user = await authenticate_user(form_data.username, form_data.password)
#     print(ACCESS_TOKEN_EXPIRE_MINUTES)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )

  
    
#     return {"access_token": access_token,  "token_type": "bearer"}
    



# @routes.get("/refresh")
# async def refresh_token(token:str=Depends(refresh_token)):