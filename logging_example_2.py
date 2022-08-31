import logging

try:
    list_1 = [1, 2, 3]
    a = list_1[4]
except IndexError as e:
    logging.error(e, exc_info=True)
