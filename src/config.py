import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

HOST_SERVER = os.getenv("HOST")
HOST_CLIENT = os.getenv("")
PORT = int(os.getenv("PORT"))
FORMAT = 'utf-8'
# ADDR = (HOST, PORT)
