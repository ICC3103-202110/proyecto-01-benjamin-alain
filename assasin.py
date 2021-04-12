from IEespecial import IEspecialAtack

class murder(IEspecialAtack):

    def __init__(self,name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "ASSASIN"
        else:
            self.__name = value
    
    def efect(self, playerlist):
        def ShowPlayers(playerlist):
            print("actual player in the game")
            for (i, _) in enumerate(playerlist):
                print(i+1,") nombre: ",playerlist[i].name,"| card: ",playerlist[i].cards)
        ShowPlayers(playerlist)
        return int(input('Who do you want to select?'))

    def counter(self):
        pass

    def MoneyLess(self, coin):
        print("pay 3 coins and eliminate a influence (show card): ")
        newcoins = coin-3
        return newcoins
    
    def action(self):
        return "assassinate"
    