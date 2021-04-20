class gambler:

    def __init__(self, name, coins,cards,points):
        self.__coins = coins
        self.__cards = cards
        self.__name = name
        self.__HandDeck = []
        self.__points = points

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
    def name(self):
        return self.__name
    @name.setter 
    def name(self,value):
        self.__name = value
        
    @property
    def coins(self):
        return self.__coins
    @coins.setter
    def coins(self, value):
        if value < 0:
            self.__coins = 0
        else:
            self.__coins = value
        
    @property
    def HandDeck(self):
        return self.__HandDeck
    @HandDeck.setter
    def HandDeck(self, value):
        self.__HandDeck = value

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, value):
        self.__points = value
    
    def AskMoney(self,option):
        if(option == 1):
            print("deberia dar 1")
        if(option == 2):
            print("deberia dar 2")
        if(option == 3):
            coin = self.coins + 3
            return coin
        if(option == 4):
            print("deberia dar -2")
        if(option == 5):
            print("deberia dar -3")
        if(option == 6):
            print("deberia dar -7")