import os
from dotenv import load_dotenv
from aiogram.fsm.state import StatesGroup, State


load_dotenv()

TOKEN=os.environ.get("TOKEN")

REDIS_CFG={
        "host":os.getenv("REDIS_HOST"),
        "port":int(os.getenv("REDIS_PORT")),
        "db":int(os.getenv("REDIS_DB")),
        }


class States(StatesGroup):
        wait_for_language = State()




languages = {
    "RU": "Russian",
    "EN": "English",
    "ES": "Spanish",
    "FR": "French",
    "DE": "German",
    "ZH": "Chinese",
    "JA": "Japanese",
    "AR": "Arabic",
    "PT": "Portuguese",
    "IT": "talian",
    "KO": "Korean",
    "HI": "Hindi",
    "TR": "Turkish",
    "NL": "Dutch",
    "SV": "Swedish"
}