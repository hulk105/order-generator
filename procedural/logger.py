import logging
from config_parser import config_parser

DEFAULT_LOG_LEVEL = logging.INFO
LOG_LEVEL = config_parser['LOG_LEVEL'].get()
NAME = 'generator'

log_levels = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
}

logger = logging.getLogger(NAME)
logger.setLevel(log_levels.get(LOG_LEVEL.upper()))
default_formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
file_handler = logging.FileHandler('order_generator.log')
file_handler.setLevel(log_levels.get(LOG_LEVEL.upper()))
file_handler.setFormatter(default_formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(DEFAULT_LOG_LEVEL)
console_handler.setFormatter(default_formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
