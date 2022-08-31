import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_info(func):
    def log_func(*args, **kwargs):
        logger.info(f"Arguments are {args}")
        fact_value = func(*args, **kwargs)
        return fact_value

    return log_func


@log_info
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        fact_value = 1
        for x in range(1, a + 1):
            fact_value = fact_value * x
    return fact_value


fact = factorial(3)
print(fact)
