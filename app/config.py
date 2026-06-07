import os
from dotenv import load_dotenv


load_dotenv()


SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_AUTH_MODE = os.getenv("SQL_AUTH_MODE", "windows")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")