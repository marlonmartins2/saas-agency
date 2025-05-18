from os import getenv

from dotenv import load_dotenv

load_dotenv()


DATABASE_ENVIRONMENT: str = getenv("DATABASE_ENVIRONMENT")
MONGO_URL: str = getenv("MONGO_URL", "mongodb")
CORS_ORIGINS: list = getenv("CORS_ORIGINS", "*").split(",")