class gambler:

    def __init__(self, coins,cards):
        self.coins = coins
        self.cards = cards
    
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, value):
        if value < 0:
            self.__cards = 0
        else:
            self.__cards = value
     
    @property
    def coins(self):
        return self.__coins
    @coins.setter
    def coins(self, value):
        if value < 0:
            self.__coins = 0
        else:
            self.__coins = value