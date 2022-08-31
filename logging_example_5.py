import logging
from logging.handlers import TimedRotatingFileHandler
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# when can 's', 'm', 'h','d', midnight, 'w01'(Monday)
handler = TimedRotatingFileHandler('Log/timed_app.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("This is info")
    time.sleep(5)