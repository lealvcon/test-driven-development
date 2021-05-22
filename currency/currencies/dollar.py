
class Dollar:
    def __init__(self, amount: int):
        self.__amount = amount

    def times(self, multiplier: int):
        return Dollar(self.__amount * multiplier)

    def equals(self, dollar) -> bool:
        return self.__amount == dollar.__amount

