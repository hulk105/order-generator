"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""
import logging
import sys

import confuse
from pathlib import Path

APP_NAME = 'order-generator-procedural'

config_logger = logging.getLogger('config parser')
config_logger.setLevel(logging.INFO)
config_logger_handler = logging.StreamHandler()
config_logger_handler.setLevel(logging.INFO)
config_logger_handler.setFormatter(logging.Formatter('%(asctime)s  %(name)s  %(levelname)s  %(message)s'))
config_logger.addHandler(config_logger_handler)

config_parser = confuse.Configuration(APP_NAME, __name__)

if Path(config_parser.config_dir(), confuse.CONFIG_FILENAME).is_file():
    config_logger.info('Config at %s/%s' % (config_parser.config_dir(), confuse.CONFIG_FILENAME))
else:
    config_logger.error('Config not found at %s' % (config_parser.config_dir()))
    sys.exit(1)
