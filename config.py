from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("DATABASE_URL")