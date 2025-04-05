import logging
from django.conf import settings

logger = logging.getLogger(__name__)
logger.setLevel(settings.LOG_LEVEL)

file_handler = logging.FileHandler(settings.LOG_FILE)
file_handler.setLevel(settings.LOG_LEVEL)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(settings.LOG_LEVEL)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
