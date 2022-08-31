import logging
import traceback

try:
    list_1 = [1, 2, 3]
    a = list_1[4]
except Exception as e:
    logging.error("The error is %s", traceback.format_exc())
