"""
Confuse searches for config.yaml at /home/user/.config/<APP_NAME>
"""

import confuse

APP_NAME = 'order-generator-procedural4'

config_parser = confuse.Configuration(APP_NAME)
