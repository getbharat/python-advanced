import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = RotatingFileHandler('Log/app.log', maxBytes=1000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.debug("Hello World")
