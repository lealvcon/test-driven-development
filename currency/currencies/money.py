class Money:

    def __init__(self, amount: int):
        self._amount = amount

    def equals(self, currency) -> bool:
        return self._amount == currency._amount
