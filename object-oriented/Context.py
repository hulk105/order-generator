from Config import OrderGeneratorConfig, YAMLConfig
from Strategies import *

generator_config = OrderGeneratorConfig(YAMLConfig('generator_data.yaml').get_config)


class Context:
    def __init__(self, strategy: FieldGeneratingStrategy) -> None:
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def get_current(self):
        return self._strategy.get_current()

    def next_entry(self):
        return self._strategy.next_entry()


order_id_context = Context(OrderIDGeneratingStrategy(generator_config.initial_order_id))
provider_id_context = Context(ProviderIDGeneratingStrategy(generator_config.provider_id))
direction_context = Context(DirectionGeneratingStrategy(generator_config.direction))
currency_pair_context = Context(CurrencyPairGeneratingStrategy(generator_config.currency_pairs))
date_context = Context(
    DateGeneratingStrategy(generator_config.zones['RED']['initial_date'], generator_config.zones['RED']['end_date'], 300)
)
status_context = Context(RandomChoiceStrategy(generator_config.zones['RED']['possible_statuses']))

for i in range(50):
    print(
        order_id_context.next_entry(),
        provider_id_context.next_entry(),
        direction_context.next_entry(),
        currency_pair_context.next_entry(),
        date_context.next_entry(),
    )
    status_context.next_entry()
    for status in status_context.get_current():
        print(
            status,
            currency_pair_context.get_strategy().delta(),
            date_context.get_current() + date_context.get_strategy().delta(),
        )