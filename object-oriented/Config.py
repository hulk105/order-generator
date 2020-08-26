from abc import ABC, abstractmethod
from yaml import load, FullLoader


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

        # self.red_zone_initial_date = config['ZONES']['RED']['initial_date']
        # self.red_zone_end_date = config['ZONES']['RED']['end_date']
        # self.red_zone_orders_percent = config['ZONES']['RED']['percent_of_total_orders']
        # self.red_zone_possible_statuses = config['ZONES']['RED']['possible_statuses']
        #
        # self.green_zone_initial_date = config['ZONES']['GREEN']['initial_date']
        # self.green_zone_end_date = config['ZONES']['GREEN']['end_date']
        # self.green_zone_orders_percent = config['ZONES']['GREEN']['percent_of_total_orders']
        # self.green_zone_possible_statuses = config['ZONES']['GREEN']['possible_statuses']
        #
        # self.blue_zone_initial_date = config['ZONES']['BLUE']['initial_date']
        # self.blue_zone_end_date = config['ZONES']['BLUE']['end_date']
        # self.blue_zone_orders_percent = config['ZONES']['BLUE']['percent_of_total_orders']
        # self.blue_zone_possible_statuses = config['ZONES']['BLUE']['possible_statuses']
