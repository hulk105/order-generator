from LCGenerator import random
from Strategies.Interface import FieldStrategy
from Strategies.Implementation import CurrencyPairStrategy, DateStrategy, VolumeStrategy


class StatusStrategy(FieldStrategy):
    def __init__(self, population: list, date_strategy: DateStrategy,
                 currency_strategy: CurrencyPairStrategy, vol_strategy: VolumeStrategy):
        self._all_possible_statuses = population
        self._current_possible_statuses = None
        self._currency_strategy = currency_strategy
        self._date_strategy = date_strategy
        self._volume_strategy = vol_strategy

        self._choice()

    def _choice(self):
        self._current_possible_statuses = random.choice(self._all_possible_statuses)

    def check_status(self, status):
        if status != "New":
            self._date_strategy.increment_change_date()
        if status == "Partially Filled":
            self._currency_strategy.delta_current()
        if status == "Rejected":
            self._volume_strategy.volume(0)

    def get_current(self):
        pass

    def next_entry(self):
        _status_list = []

        self._choice()

        for status in self._current_possible_statuses:
            self.check_status(status)
            print(status, self._currency_strategy.get_current(), self._volume_strategy.get_current())
            _status_list.append(
                [status, str(self._date_strategy.get_current()),
                 self._currency_strategy.get_current(), self._volume_strategy.get_current()]
            )
        self._currency_strategy.next_entry()
        self._volume_strategy.next_entry()
        return _status_list
