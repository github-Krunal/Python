import logging
import logger_config   # this sets up logging once

def add(a,b):
    logging.debug('addition operation taking place')
    return a+b

logging.debug('addition operation is called')
add(2,3)