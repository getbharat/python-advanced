import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Log:

    def __init__(self):
        pass

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            logger.info(f"Argument are {args}")
            result = fn(*args, **kwargs)
            print("End")
            return result

        return wrapper


@Log()
def add(a, b):
    return a + b


value = add(5, 6)

print(value)
