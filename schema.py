from tortoise import Tortoise, run_async
from app.Database.connectToDatabase import connectTodatbase
async def main():
    await connectTodatbase()
    await Tortoise.generate_schemas()
if __name__ == '__main__':
    run_async(main())