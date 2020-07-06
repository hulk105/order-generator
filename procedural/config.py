"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""
import os

import confuse
import logging

APP_NAME = 'order-generator-procedural'

config_parser = confuse.Configuration(APP_NAME, __name__)

LOG_LEVEL = config_parser['LOG_LEVEL'].get(str)


logging_levels = {
    'CRITICAL': logging.CRITICAL,
    'ERROR': logging.ERROR,
    'WARNING': logging.WARNING,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
}


def setup_logger():
    try:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging_levels[LOG_LEVEL.upper()])
        logging.info('Logging level set to: %s', LOG_LEVEL.upper())
    except KeyError:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
        logging.error('Invalid log level specified: %s', LOG_LEVEL)
        logging.info('Log level: %s', logging.getLevelName(logging.INFO))


# logging.info('Config: %s' % config_parser.config_dir(), confuse.CONFIG_FILENAME)

# logging.debug('Configuration at %s/%s', config_parser.config_dir(), confuse.CONFIG_FILENAME)

# config_filename = os.path.join(config.config_dir(),
#                                confuse.CONFIG_FILENAME)
# with open(config_filename, 'w') as f:
#     yaml.dump(migrated_config, f)
