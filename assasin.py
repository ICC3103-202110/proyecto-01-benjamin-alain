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
            self.__name = "ASSASIN"
    
    def efect(self, playerlist,CoinList, cards,n):
        L = []
        x = 0
        while(x<n):
            fila = [str(x)+". Jugador: "+playerlist[x]+"| monedas: "+str(CoinList[x])+"| cartas"+str(cards[x])]
            L.append(fila)
            x += 1
        L.pop(0)
        for i in range(len(L)):
            print(L[i]) 
        return ""
        
    def counter(self):
        pass
    '''
    def MoneyLess(self, coin):
        print("pay 3 coins and eliminate a influence (show card): ")
        newcoins = coin-3
        return newcoins
    '''
    def action(self):
        return "assassinate"
    