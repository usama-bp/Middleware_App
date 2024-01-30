import os
from dotenv import load_dotenv



load_dotenv()


username=os.getenv("USERNAME")
dbname=os.getenv("DATABASENAME")
port=os.getenv("PORT")
host=os.getenv("HOST")
password=os.getenv("PASSWORD")





TORTOISE_ORM={

"connections": {"default": f"postgres://{username}:{password}@{host}:{port}/{username}"},
"apps": {   "models": {
    "models": ["app.models.model", "aerich.models"],
    "default_connection": "default",
},
},
}