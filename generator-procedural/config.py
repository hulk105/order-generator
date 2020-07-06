"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""
import os

import confuse
import logging

APP_NAME = 'order-generator-procedural'

config_parser = confuse.Configuration(APP_NAME, __name__)

LOG_LEVEL = config_parser['LOG_LEVEL']

# logging.debug('Configuration at %s/%s', config_parser.config_dir(), confuse.CONFIG_FILENAME)

# config_filename = os.path.join(config.config_dir(),
#                                confuse.CONFIG_FILENAME)
# with open(config_filename, 'w') as f:
#     yaml.dump(migrated_config, f)
