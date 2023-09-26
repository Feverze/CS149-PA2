"""This module defines the PortfolioCoin class.

The PortfolioCoin class stores info about a coin in a portfolio.

Author: Frankie Benedetto
Honor Code: My work complies with the JMU Honor Code and instructions for this assignment.
"""


class PortfolioCoin:
    """The PortfolioCoin class creates a portfolio of a coin.

    Attributes:
        _price_paid_per_coin (float): how much was paided for the coin at current price.
        _coin (str): the actual coin that the portfolio is being made after.
        _amount_owned (float): the amount owned.
    """
    def __init__(self, coin, price_paid_per_coin, amount_owned):
        self._coin = coin
        self._price_paid_per_coin = price_paid_per_coin
        self._amount_owned = amount_owned

    def get_coin(self):
        return self._coin

    def set_coin(self, coin):
        self._coin = coin

    def get_price_paid_per_coin(self):
        return self._price_paid_per_coin

    def set_price_paid_per_coin(self, price_paid_per_coin):
        self._price_paid_per_coin = price_paid_per_coin

    def get_amount_owned(self):
        return self._amount_owned

    def set_amount_owned(self, amount_owned):
        self._amount_owned = amount_owned

    def get_total_price_paid(self):
        """Tells you the total price paid for said coin.

        Returns:
            float: Total price paid.
        """
        return self._price_paid_per_coin * self._amount_owned

    def get_current_value(self):
        """Tells you the current value of a coin.

        Returns:
            float: Current value.
        """
        return self._coin.get_price() * self._amount_owned

    def get_current_gain_loss(self):
        """Returns the gain or loss of money on a coin.

        Returns:
            float: Amount profit or lost.
        """
        return self.get_current_value() - self.get_total_price_paid()

    def __eq__(self, other):
        if isinstance(other, PortfolioCoin):
            return self._coin == other._coin and self._amount_owned == other._amount_owned
        return False

    def __str__(self):
        return f"{self._amount_owned:.4f} {self._coin.get_symbol()} coins were purchased \
at {self._price_paid_per_coin:.10f} per coin.\n{str(self._coin)}\n"
