from tortoise import fields
from tortoise.models import Model
from passlib.context import CryptContext




class Users_(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=255)
    username=fields.CharField(max_length=255,unique=True)
    password=fields.CharField(max_length=255)
    created_at=fields.DatetimeField(auto_now_add=True)
    updated_at=fields.DatetimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    # async def setpassword(self):
    #     myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
    #     self.password=myctx.hash(self.password)
    #     await self.save()
    async def check_pass(self,password):
        myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

        return myctx.verify(password,self.password)
    
class Customer(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=255)
    shop_name=fields.CharField(max_length=255,unique=True)
    add_by=fields.ForeignKeyField('models.Users_',related_name='customer',on_delete=fields.CASCADE)
    created_at=fields.DatetimeField(auto_now_add=True)
    updated_at=fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.name

