from deta import Deta
import os
from dotenv import load_dotenv
load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY")
deta = Deta(DETA_KEY)
db = deta.Base("mymsg")
def insert(msg, mid):
    return db.put({"key": mid, "message": msg})