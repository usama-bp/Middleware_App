from pydantic import BaseModel
# from ..models.model import Users_
from passlib.context import CryptContext


class User_s(BaseModel):
    name: str
    username: str
    password: str

    # def hash_password(self):
def savepassword(password): 
      myctx = CryptContext(schemes=["sha256_crypt", "md5_crypt"])
      password=myctx.hash(password)

      return password
        
class customer_s(BaseModel):
    name: str
    shop_name: str
    add_by_id: int
    