import logging

logger = logging.getLogger(__name__)
# logger.propagate = False  # Logs  would not propagate to the base logger
# logger.info('info from log-helper')

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

formatter = logging.Formatter(fmt='%(name)s - %(levelname)s - %(message)s')
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.warning('This is warning')
logger.error('This is error')