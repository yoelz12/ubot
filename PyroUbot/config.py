import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "1286240629").split()))

API_ID = int(os.getenv("API_ID", "29984284"))

API_HASH = os.getenv("API_HASH", "c41d118adb5d91352aa6eac8586a3f00")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8018053694:AAFJj9K4qeqR0NElLA7P620Yt-hq4RRqq6U")

OWNER_ID = int(os.getenv("OWNER_ID", "1286240629"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aortulsk:KxCX5EQdssavL4dm@cluster0.qsywpr2.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4917438098"))
