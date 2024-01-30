from fastapi import FastAPI,Request,HTTPException
from app.api.apis import router as main_router
from tortoise.contrib.fastapi import register_tortoise
from app.Database.connectToDatabase import connectTodatbase,closeDatabase
from contextlib import asynccontextmanager
# from app.middlewares.midddlewares import checkuser
import time


@asynccontextmanager
async def life_span(app: FastAPI):
    
        await connectTodatbase()
        yield
        await closeDatabase()




async def checkdata(request:Request):
        data=True

        if request:
                return "True"
        else:
                return "False"

        
        
        


app = FastAPI(lifespan=life_span)

# app.add_middleware(loginMiddleware)





app.include_router(main_router)

register_tortoise(
    app,
    db_url="postgres://usamarehman:admin@localhost:5432/usamarehman",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)