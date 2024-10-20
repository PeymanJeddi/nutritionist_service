# models.py
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    name: str
    age: int
    weight: float
    height: float
    job: str
    workout_routine: str

class CalorieEntry(BaseModel):
    user_id: str
    date: str
    food_description: str
    total_calories: float
