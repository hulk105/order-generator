from abc import ABC, abstractmethod
from yaml import load, FullLoader

GENERATOR_CONFIG_VALID_TYPES = {
    'TOTAL_ORDER': type(int),
    'INITIAL_ORDER_ID': type(str),
    'PROVIDER_ID': type(list),
    'DIRECTION': type(list),
    'CURRENCY_PAIR': type(dict),
    'ZONES': type(dict)
}


class Config(ABC):
    @abstractmethod
    def _parse_config(self, config_file_path):
        pass

    def get_config(self):
        pass


class YAMLConfig(Config):
    def __init__(self, file_path: str):
        self._config = self._parse_config(file_path)

    def _parse_config(self, config_file_path):
        return load(open(config_file_path), Loader=FullLoader)

    @property
    def get_config(self):
        return self._config


class OrderGeneratorConfig:
    def __init__(self, config: dict):
        self.config = config
        self.total_orders = config['TOTAL_ORDERS']
        self.initial_order_id = config['INITIAL_ORDER_ID']
        self.provider_id = config['PROVIDER_ID']
        self.direction = config['DIRECTION']
        self.currency_pairs = list(config['CURRENCY_PAIR'].items())
        self.zones = config['ZONES']