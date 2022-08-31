import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def log_info(func):
    def log_details(*args, **kwargs):
        logger.info(f"Arguments are {args}")
        print(func(*args, **kwargs))
    return log_details


@log_info
def add_nums(a, b):
    return a + b


add_nums(2, 3)
