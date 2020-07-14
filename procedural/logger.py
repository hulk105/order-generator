import logging

from config_parser import config_parser, APP_NAME

DEFAULT_LOG_LEVEL = logging.INFO
log_levels = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
}
LOG_LEVEL = log_levels.get(config_parser['LOG_LEVEL'].get().upper())

if LOG_LEVEL is None:
    LOG_LEVEL = DEFAULT_LOG_LEVEL

logger = logging.getLogger(APP_NAME)
logger.setLevel(LOG_LEVEL)
default_formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s')
file_handler = logging.FileHandler('order_generator.log')
file_handler.setLevel(LOG_LEVEL)
file_handler.setFormatter(default_formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(default_formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('Log level set up to %s' % logging.getLevelName(logger.level))

