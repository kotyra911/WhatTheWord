import os


API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("API_KEY", "gpt-4")
TIMEOUT = int(os.getenv("AI_TIMEOUT", "15"))