import logging

from logger import logger
from order_history_generator import generator


def init():
    pass


def setup():
    # TODO Setup logger and config here
    pass


def workflow():
    logger.info('Generator started')
    try:
        generator.generate_order_history()
        generator.write_sql_dump()
    except Exception as e:
        logger.error(e)


def result():
    generator.show_total()


if __name__ == '__main__':
    init()
    setup()
    workflow()
    result()
