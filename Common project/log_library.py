import logging
from time import asctime

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s:%(message)s')

file_handler=logging.FileHandler('funct1.log')
stream_handler=logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# logging.basicConfig(filename='logging.log',level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logger.info('hello')