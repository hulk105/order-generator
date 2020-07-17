import logging

import yaml

import constants as const
from order_history_generator import generator


def init():
    pass


def setup():
    pass


def setup_logger():
    logging.basicConfig(level=logging.DEBUG, filename=const.LOG_FILENAME, format=const.LOG_DEFAULT_FORMAT)


def workflow():
    logging.info(const.APP_NAME + 'started')
    generator.generate_order_history()


def output():
    generator.show_total()
    logging.info('Done')


if __name__ == '__main__':
    init()
    setup_logger()
    workflow()
    output()
