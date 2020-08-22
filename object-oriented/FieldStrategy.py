from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass


class IncrementalFieldStrategy(Strategy):
    def do_algorithm(self):
        return "This is incremental"


class RandomFieldStrategy(Strategy):
    def do_algorithm(self):
        return "This is random"


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        return self._strategy.do_algorithm()


context = Context(IncrementalFieldStrategy())
print(context.do_some_business_logic())
print(context.strategy)
