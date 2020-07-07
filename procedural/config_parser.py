"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""
import confuse
import logging

APP_NAME = 'order-generator-procedural'

config_logger = logging.getLogger('config parser')
config_logger_handler = logging.StreamHandler()
config_logger.addHandler(config_logger_handler)
config_parser = confuse.Configuration(APP_NAME, __name__)
config_logger.info('Config at %s/%s' % (config_parser.config_dir(), confuse.CONFIG_FILENAME))
