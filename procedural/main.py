import logging

from logger import logger
from order_history_generator import generator


def init():
    pass


def setup():
    logger.info('Log level set up to %s' % logging.getLevelName(logger.level))


def workflow():
    logger.info('%s started', __name__)
    try:
        generator.set_random_seed()
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
