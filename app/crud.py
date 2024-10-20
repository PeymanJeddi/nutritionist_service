# app/crud.py
from app.database import user_collection

# Helper function to convert MongoDB document to the specified response format
def user_data_helper(user_data) -> dict:
    return {
        "useremail": user_data["useremail"],
        "calories": [
            {
                "date": daily_calorie["date"],
                "snacks": daily_calorie.get("snacks"),
                "breakfast": daily_calorie.get("breakfast"),
                "lunch": daily_calorie.get("lunch"),
                "dinner": daily_calorie.get("dinner")
            } for daily_calorie in user_data["calories"]
        ]
    }

# Create a new user data entry
async def create_user_data(user_data: dict) -> dict:
    new_user_data = await user_collection.insert_one(user_data)
    created_user_data = await user_collection.find_one({"_id": new_user_data.inserted_id})
    return user_data_helper(created_user_data)

# Get user data by email
async def get_user_data(useremail: str) -> dict:
    user_data = await user_collection.find_one({"useremail": useremail})
    if user_data:
        return user_data_helper(user_data)
    return None

# Update user data by email
async def update_user_data(useremail: str, data: dict) -> bool:
    user_data = await user_collection.find_one({"useremail": useremail})
    if user_data:
        updated_user_data = await user_collection.update_one(
            {"useremail": useremail}, {"$set": data}
        )
        if updated_user_data.modified_count > 0:
            return True
    return False

# Delete calorie data by email and date
async def delete_calorie_data(useremail: str, date: str) -> bool:
    user_data = await user_collection.find_one({"useremail": useremail})
    if not user_data:
        return False

    # Filter out the calorie data for the specified date
    updated_calories = [
        daily_calorie for daily_calorie in user_data["calories"]
        if daily_calorie["date"] != date
    ]

    # Update the user's calorie data in the database
    result = await user_collection.update_one(
        {"useremail": useremail},
        {"$set": {"calories": updated_calories}}
    )
    return result.modified_count > 0
