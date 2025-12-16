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
        are_you_sure = State()
        wait_for_words = State()

funny_photo="AgACAgIAAxkBAAIXHWlBUTf1v1YDZVH_adBWXBkX_PJGAAKID2sbiREJStoc7xGA_M2BAQADAgADeQADNgQ"


languages = {
    "RU": "Russian",
    "EN": "🇺🇸 — English",
    "ES": "🇪🇸 — Spanish",
    "FR": "🇫🇷 — French",
    "DE": "🇩🇪 — German",
    "ZH": "🇨🇳 — Chinese",
    "JA": "🇯🇵 — Japanese",
    "AR": "🇸🇦 — Arabic",
    "PT": "🇵🇹 — Portuguese",
    "IT": "🇮🇹 — Italian",
    "KO": "🇰🇷 — Korean",
    "HI": "🇮🇳 — Hindi",
    "TR": "🇹🇷 — Turkish",
    "NL": "🇳🇱 — Dutch",
    "SV": "🇸🇪 — Swedish"
}