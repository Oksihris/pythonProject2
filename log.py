import logging
import traceback

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')

logger = logging.getLogger(__name__)
logger.info('HELLO')


import logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('HELLO')

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Configure level and formatter and add it to handlers
stream_handler.setLevel(logging.WARNING) # warning and above is logged to the stream
file_handler.setLevel(logging.ERROR) # error and above is logged to a file

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error') # logged to the stream AND the file!


class InfoFilter(logging.Filter):
    
    # overwrite this method. Only log records for which this
    # function evaluates to True will pass the filter.
    def filter(self, record):
        return record.levelno == logging.INFO

# Now only INFO level messages will be logged
stream_handler.addFilter(InfoFilter())
logger.addHandler(stream_handler)

try:
    a = [1, 2, 3]
    value = a[3]
except IndexError as e:
    logging.error(e)
    logging.error(e, exc_info=True)

try:
    a = [1, 2, 3]
    value = a[3]
except:
    logging.error("uncaught exception: %s", traceback.format_exc())

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')

import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)

