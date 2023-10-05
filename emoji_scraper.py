from db_base import community_tibero
from db_insert import *
import logging
import logging.handlers
import requests
from time import sleep
from bs4 import BeautifulSoup
import json

filehandler = logging.handlers.TimedRotatingFileHandler(filename='nate_logfile_', when='midnight', interval=1,
                                                        encoding='utf-8')
filehandler.suffix = "%Y%m%d"
filehandler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s'))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(filehandler)

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/87.0.4280.66 "
    "Safari/537.36"
)

db = community_tibero()
cursor = db.cursor()
nav_url = "https://cdn.jsdelivr.net/npm/emojibase-data@latest/ko/data.json"

def _emoji_scraper():
    try:
        req = requests.get(nav_url, headers={"user-agent": USER_AGENT})
        if req.status_code == 200:
            json_decoded = json.loads(req.text)
            pass
    except Exception as e:
        logger.info(f'{e} error occur')
