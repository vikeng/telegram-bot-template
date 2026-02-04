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
h = hashlib.sha256()
h.update(TOKEN.encode('utf-8'))
WEBHOOK_SECRET = h.hexdigest()
WEBHOOK_URL = f"{BASE_URL}/{WEBHOOK_SECRET}"

