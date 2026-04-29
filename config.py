import os
from dotenv import load_dotenv
load_dotenv()
class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    POSTGRES_URL = os.getenv("POSTGRES_URL")
    REDIS_URL = os.getenv("REDIS_URL")
settings = Settings()
