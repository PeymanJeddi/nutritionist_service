# database.py
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"  # The MongoDB connection string

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.nutritionist_db

user_collection = database.get_collection("users")
calorie_collection = database.get_collection("calories")
