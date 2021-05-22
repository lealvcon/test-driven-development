from currency.currencies.money import Money


class Dollar(Money):
    def __init__(self, amount: int):
        super(Dollar, self).__init__(amount)

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)
