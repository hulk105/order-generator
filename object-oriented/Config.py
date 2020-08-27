from abc import ABC, abstractmethod
from yaml import load, FullLoader
from Exceptions import InvalidConfigurationError

GENERATOR_CONFIG_VALID_TYPES = {
    'TOTAL_ORDERS': 123,
    'INITIAL_ORDER_ID': 'str',
    'PROVIDER_ID': [],
    'DIRECTION': [],
    'CURRENCY_PAIR': {str: 1.1},
    'ZONES': {},
    'TAGS': []
}


def iterate_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            iterate_dict(v)
        else:
            print(k, ":", v)


def validate_config_structure(validated, validator):
    for key, value in validated.items():
        if isinstance(value, dict):
            validate_config_structure(value, validator)
        else:
            print(key, value)


class Config(ABC):
    @abstractmethod
    def _parse_config(self, config_file_path):
        pass

    def get_config(self):
        pass


class YAMLConfigProvider(Config):
    def __init__(self, file_path: str):
        self._config = self._parse_config(file_path)

    def __getitem__(self, item):
        return self._config[item]

    def _parse_config(self, config_file_path):
        return load(open(config_file_path), Loader=FullLoader)

    @property
    def get_config(self) -> dict:
        return self._config


class OrderGeneratorConfig:
    def __init__(self, config: dict):
        self.config = config
        self.total_orders = config['TOTAL_ORDERS']
        self.initial_order_id = config['INITIAL_ORDER_ID']
        self.provider_id = config['PROVIDER_ID']
        self.direction = config['DIRECTION']
        self.currency_pairs = config['CURRENCY_PAIR']
        self.zones = config['ZONES']
        self.tags = config['TAGS']

    def config(self, config: dict):
        self.config = config
