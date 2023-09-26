"""This module defines the Portfolio class.

The Portfolio class is part B.

Author: Frankie Benedetto
Honor Code: No help just me.
"""
from portfolio_coin import PortfolioCoin
from market import Market
from coin import Coin


class Portfolio:
    """The portfolio class is the users portfolio of coins.

    It is important cause its all of part B.

    Attributes:
        _market: Market.
        _coins: PortfolioCoin
    """
    def __init__(self, market):
        self._coins = []
        self._market = market
        
    def add_coin(self, coin_data):
        coin_symbol, price_paid, amount_owned = coin_data
        if coin_symbol not in Market._load_coin_list(self):
            return False
        if price_paid is None or price_paid <= 0 or price_paid > 250000:
            return False
        if amount_owned is None or amount_owned <= 0 or amount_owned > 1000000:
            return False
        x = PortfolioCoin(coin_symbol, price_paid, amount_owned)
        self._coins.append(x)
        return True
    
    def add_coins(self, coin_data):
        for coin in coin_data:
            self.add_coin(coin) 
    
    def get_orginal_value(self):
        return sum(x.get_total_price_paid() for x in self._coins)
    
    def get_current_value(self):
        return sum(x.get_current_value() for x in self.coins)
    
    def get_gain_loss(self):
        OG = self.get_orginal_value()
        CV = self.get_current_value()
        if OG is None or CV is None:
            return 0.0
        return CV - OG
           
    def get_best_earner(self):
        if not self._coins:
            return None  
        best = self._coins[0]
        for x in self._coins:
            if x.get_current_gain_loss() > best.get_current_gain_loss():
                best = x
            return best

    def get_worst_earner(self):
        if not self._coins:
            return None  
        worst = self._coins[0]
        for x in self._coins:
            if x.get_current_gain_loss() < worst.get_current_gain_loss():
                worst = x
            return worst
            
    def get_coin(self, symbol):
        for x in self._coins:
            if x.get_symbol == symbol:
                return x
        return None
    
    def __str__(self):
        strings = '\n'.join(str(x) for x in self._coins)
        return (f"Portfolio contains {len(self._coins)} cryptocurrencies.\n"
                f"The purchase cost of the portfolio was ${self.get_original_value():.2f}"
                f" and the current value is ${self.get_current_value():.2f}.\n"
                f"{strings}")

    def search_coins(self, search):
        search = search.lower() 
        results = []
        for coin in Market.coins:
            description = coin.get_description().lower() 
            if search in description:
                words = description.split()
                index = words.index(search)
                start_index = max(0, index - 3)
                end_index = min(len(words), index + 4)
                substring = ' '.join(words[start_index:end_index])
                results.append(f"{coin.get_symbol()}: {substring}\n")
        return ''.join(results)
        
    