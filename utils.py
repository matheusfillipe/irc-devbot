from functools import wraps
from settings import *


# COMMAND DECORATORS
regex_commands=[]
def regex_cmd(filters, **kwargs):
    def wrap_cmd(func):
        @wraps(func)
        def wrapped (*a, **bb):
            return func(*a, **bb)
        regex_commands.append({filters: func})
        return wrapped
    return wrap_cmd

url_commands=[]
def url_handler(**kwargs):
    def wrap_cmd(func):
        @wraps(func)
        def wrapped (*a, **bb):
            return func(*a, **bb)
        url_commands.append(func)
        return wrapped
    return wrap_cmd



# LOGGING SETUP
import logging
from settings import *
logging.basicConfig(level=LEVEL, filename=LOGFILE)
logger = logging.getLogger()
logger.setLevel(LEVEL)

def log(*args, level=LEVEL):
    msg=" ".join([str(a) for a in list(args)])
    if type(LEVEL)==int:
        logger.log(LEVEL, msg)
    elif type(LEVEL)==str:
        getattr(logger, level)(msg)


def debug(*args, level=LEVEL):
    msg=" ".join([str(a) for a in list(args)])
    logger.log(logging.DEBUG, msg)

import validators
def validateUrl(url):
    return validators.url(url)
