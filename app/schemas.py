# app/schemas.py
from typing import List, Optional
from pydantic import BaseModel

# Meal content schema
class MealContent(BaseModel):
    name: str

# Meal schema
class Meal(BaseModel):
    total_calories: float
    meal_content: List[MealContent]

# Daily calorie schema
class DailyCalorie(BaseModel):
    date: str
    snacks: Optional[Meal] = None
    breakfast: Optional[Meal] = None
    lunch: Optional[Meal] = None
    dinner: Optional[Meal] = None

# User data schema for creating and updating user data
class UserData(BaseModel):
    useremail: str
    calories: List[DailyCalorie]

# UserDataResponse adjusted to match the response format from the helper function
class UserDataResponse(BaseModel):
    useremail: str
    calories: List[DailyCalorie]
