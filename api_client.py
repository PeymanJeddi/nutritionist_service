import requests

BASE_URL = "http://104.194.158.124:8001"  # Your FastAPI base URL

def create_user_data(user_data):
    """Create new user data via API."""
    response = requests.post(f"{BASE_URL}/data", json=user_data)
    return response.json()

def get_user_data(user_email):
    """Fetch user data by email via API."""
    response = requests.get(f"{BASE_URL}/data/{user_email}")
    return response.json()

def update_user_data(user_email, updated_data):
    """Update user data by email via API."""
    response = requests.put(f"{BASE_URL}/data/{user_email}", json=updated_data)
    return response.json()

def delete_user_data(user_email, date):
    """Delete user data by email and date via API."""
    response = requests.delete(f"{BASE_URL}/data/{user_email}/{date}")
    return response.json()
