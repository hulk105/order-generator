from Config import OrderGeneratorConfig
from Factory.Interface import AbstractGenerator
from Strategies.Implementation import *
from Constants import *


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
        self._orders_list = None

    def generate_objects(self):
        self._orders_list = []
        for zone in self._config.zones:
            _date = DateStrategy(
                initial_date=self._config.zones[zone][ZONE_INITIAL_DATE_KEY],
                end_date=self._config.zones[zone][ZONE_END_DATE_KEY],
                steps=self._config.total_orders * self._config.zones[zone][ZONE_PERCENT_OF_TOTAL_ORDERS_KEY])
            _status = StatusStrategy(population=self._config.zones[zone][ZONE_POSSIBLE_STATUSES_KEY],
                                     date_strategy=_date,
                                     currency_strategy=self._currency_pair, vol_strategy=self._volume_strategy)
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
