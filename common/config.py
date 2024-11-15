from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_TOKEN = os.getenv("API_TOKEN")
DEBUG = os.getenv("DEBUG", False) == True

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}