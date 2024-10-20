# app/main.py
from fastapi import FastAPI, HTTPException
from app.crud import create_user_data, get_user_data, update_user_data, delete_calorie_data
from app.schemas import UserDataResponse, UserData

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Nutritionist API!"}

# Create user data
@app.post("/data", response_model=UserData)
async def create_user_data_endpoint(user_data: UserData):
    created_user_data = await create_user_data(user_data.dict())
    return created_user_data

# Get user data by email in the specified format
@app.get("/data/{useremail}", response_model=UserDataResponse)
async def get_user_data_endpoint(useremail: str):
    user_data = await get_user_data(useremail)
    if user_data:
        return user_data
    raise HTTPException(status_code=404, detail="User data not found")

# Update user data by email
@app.put("/data/{useremail}", response_model=UserData)
async def update_user_data_endpoint(useremail: str, user_data: UserData):
    updated = await update_user_data(useremail, user_data.dict(exclude_unset=True))
    if updated:
        return await get_user_data(useremail)
    raise HTTPException(status_code=404, detail="User data not found")

# Delete calorie data by email and date
@app.delete("/data/{useremail}/{date}")
async def delete_calorie_data_endpoint(useremail: str, date: str):
    deleted = await delete_calorie_data(useremail, date)
    if deleted:
        return {"message": f"Calorie data for date {date} deleted successfully"}
    raise HTTPException(status_code=404, detail="Calorie data not found for the specified date")
