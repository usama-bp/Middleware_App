from tortoise import Tortoise

pathh='app\models\model.py'
async def connectTodatbase():
    await Tortoise.init(
        db_url='postgres://usamarehman:admin@localhost:5432/usamarehman',
        modules={'models': ['app.models.model']}
    )
    await Tortoise.generate_schemas()
    return Tortoise
async def closeDatabase():
    await Tortoise.close_connections()
    return Tortoise