from fastapi import APIRouter
from ..models.model import Users_
from tortoise.contrib.pydantic import pydantic_model_creator
from ..pydantic_model.schemaModel import User_s,savepassword


pydanticuser=pydantic_model_creator(Users_)

routes = APIRouter()


@routes.get("/")
async def get_users():
    allusers=await Users_.all()
    for user in allusers:
         orderd=[{
             "id": user.id,
            "name": user.name,
            "username": user.username,
            "password": user.password
        }]
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



@routes.post("/login/")
async def login(users:User_s):
    user=await Users_.get(username=users.username)
    if user:
        if await user.check_pass(users.password):
            return {"message":"login successfull"}
        else:
            return {"message":"password is wrong"}
    else:
        return {"message":"user not found"}

