
class Franc:
    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Franc(self.__amount * multiplier)

    def equals(self, franc) -> bool:
        return self.__amount == franc.__amount