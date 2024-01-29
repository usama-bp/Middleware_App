from fastapi import APIRouter,HTTPException
from ..models.model import Customer,Users_
from tortoise.contrib.pydantic import pydantic_model_creator
from ..pydantic_model.schemaModel import customer_s
import json
import json

# Assuming `orderd` is the queryset you want to convert to a dictionary

# Now `orderd_dict` contains the dictionary representation of the queryset in JSON format

pydantic_customer=pydantic_model_creator(Customer)




router= APIRouter()

@router.get("/")
async def get_customer():
    try:
        allcustomer=await Customer.all()
        # print(type(allcustomer))
        # orderd_dict = json.loads(json.dumps(allcustomer))
        
        # orderd=[]
        
        return allcustomer
    except Exception as e:
        return HTTPException(status_code=400,detail=str(e))

@router.post("/addcustomer/")
async def create_customer(customer:customer_s):
    user=await Users_.get(id=customer.add_by_id)
    if user:
        cust=await Customer.create(name=customer.name,shop_name=customer.shop_name,add_by=user)
        return {"message":"customer created"}
    else:
        return {"message":"user not found"}
    