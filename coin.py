"""This module defines the Coin class.

The Coin class is a Coin object, which represents a cryptocurrency.

Author: Frankie Benedetto
Honor Code: No help just me.
"""


class Coin:
    """The coin class just holds the coin that is basically under observation.

    It is needed in the market file thus it is important.

    Attributes:
        _symbol (str): The symbol of the coin.
        _name (str): Name of the coin.
        _price (float): Price of the coin.
        _description (str): Description of the coin.
    """
    def __init__(self, symbol, name, price):
        self._symbol = symbol
        self._name = name
        self._price = price
        self._description = ""
                
    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def __eq__(self, other):
        if isinstance(other, Coin):
            return self._symbol == other._symbol and self._name == other._name
        return False

    def __str__(self):
        return f"{self._symbol}: {self._name} is trading at {self._price:.10f}\n{self._description}"
