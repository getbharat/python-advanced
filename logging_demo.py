import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s -%(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%H:%S')
import logging_helper
logging.debug('This is debug')
logging.info("This is info")
logging.warning("This is warn")
logging.error("This is error")
logging.critical("This is fatal")

