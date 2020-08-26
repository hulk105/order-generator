from abc import ABC, abstractmethod

from Config import OrderGeneratorConfig
from Strategies.Implementation import *


class GeneratorFactory(ABC):
    @abstractmethod
    def create_generator(self, config):
        pass


class OrderHistoryGeneratorFactory(GeneratorFactory):
    def create_generator(self, config):
        return OrderHistoryGenerator(config)


class AbstractGenerator(ABC):
    @abstractmethod
    def generate_objects(self):
        pass


class OrderHistoryGenerator(AbstractGenerator):
    def __init__(self, config: OrderGeneratorConfig):
        self._config = config
        self._order_id = OrderIDStrategy(self._config.initial_order_id)
        self._provider_id = ProviderIDStrategy(self._config.provider_id)
        self._direction = DirectionStrategy(self._config.direction)
        self._currency_pair = CurrencyPairStrategy(self._config.currency_pairs)
        self._volume_strategy = VolumeStrategy()
        self._description = DescriptionStrategy()
        self._tags = TagsStrategy(self._config.tags)
        self._extra_data = ExtraDataStrategy()
        self._orders_list = []

    def generate_objects(self):
        for zone in self._config.zones:
            _date = DateStrategy(
                initial_date=self._config.zones[zone]['initial_date'],
                end_date=self._config.zones[zone]['end_date'],
                steps=self._config.total_orders * self._config.zones[zone]['percent_of_total_orders']
            )
            _status = StatusStrategy(population=self._config.zones[zone]['possible_statuses'],
                                     date_strategy=_date,
                                     currency_strategy=self._currency_pair,
                                     vol_strategy=self._volume_strategy
                                     )

            for _ in range(self._config.total_orders):
                self._orders_list.append(
                    [
                        self._order_id.next_entry(),
                        self._provider_id.next_entry(),
                        self._direction.next_entry(),
                        self._tags.next_entry(),
                        _date.next_entry(),
                        _status.next_entry()
                    ]
                )

    def get_orders_list(self):
        return self._orders_list
