import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost/the_cheap_wanderer")
LLM_API_KEY = os.getenv("LLM_API_KEY", "your-llama-2-api-key")
