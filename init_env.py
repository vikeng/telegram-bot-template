import hashlib, os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("PROD") == "True":
    PROD = True
else:
    PROD = False
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")
PORT = int(os.getenv("PORT"))
WEBHOOK_URL = f"{BASE_URL}/{TOKEN}"

