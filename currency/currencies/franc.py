from currency.currencies.money import Money


class Franc(Money):
    def __init__(self, amount: int):
        super(Franc, self).__init__(amount)

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
