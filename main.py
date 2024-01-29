from fastapi import FastAPI
from app.api.apis import router as main_router
from tortoise.contrib.fastapi import register_tortoise
from app.Database.connectToDatabase import connectTodatbase,closeDatabase
from contextlib import asynccontextmanager


@asynccontextmanager
async def life_span(app: FastAPI):
    
        await connectTodatbase()
        yield
        await closeDatabase()






app = FastAPI(lifespan=life_span)



app.include_router(main_router)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)