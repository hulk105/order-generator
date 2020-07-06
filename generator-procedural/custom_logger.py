import logging

try:
    import colorlog
except ImportError:
    pass


def setup_custom_logger(name):
    try:
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            "%(black)s%(asctime)s%(reset)s%(log_color)s %(levelname)s %(reset)s%(message_log_color)s%(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'bold_yellow',
                'ERROR': 'red',
                'CRITICAL': 'bg_red,bold_black',
            },
            secondary_log_colors={
                'message': {
                    'DEBUG': 'cyan',
                    'INFO': 'white',
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red',
                },
            },
            style='%'
        ))
        logger = colorlog.getLogger(name)
        logger.addHandler(handler)
        try:
            logger.setLevel(logging_levels.get(LOGGING_LEVEL.upper()))
            logger.log(level=logging.INFO, msg='Log level set to: ' + LOGGING_LEVEL.upper())
            return logger
        except TypeError:
            logger.error('Invalid log level specified in config: ' + str(LOGGING_LEVEL))
            logger.setLevel(logging.INFO)
            logger.warning('Setting log level to ' + 'INFO ' + str(logging.INFO))
            return logger
    except Exception:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)
        return logger
