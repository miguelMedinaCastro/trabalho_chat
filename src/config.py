from .lib import os
from .lib import load_dotenv
from .lib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

HOST_SERVER = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
FORMAT = 'utf-8'
