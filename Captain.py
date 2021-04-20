from IEespecial import IEspecialAtack
from random import shuffle

class Steal(IEspecialAtack):

    def __init__(self, name):
        self.__name = name
           
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "Captain"
        else:
            self.__name = "Captain"
    
    def efect(self, playerlist,optionnum,CoinList,n):
        def ShowPlayers(playerlist):
            print("actual player in the game")
            for (i, _) in enumerate(playerlist):
                print(i+1,") nombre: ",playerlist[i].name,"| card: ",playerlist[i].cards)
        def objetives(playerlist,CoinList,n):
            x = 0
            L = []
            while(x<n):
                fila = [str(x)+". Jugador: "+playerlist[x]+"| monedas: "+str(CoinList[x])]
                L.append(fila)
                x += 1
            L.pop(0)
            for i in range(len(L)):
                print(L[i])          
        if (optionnum == 0):
            ShowPlayers(playerlist)
        elif(optionnum == 1):
            objetives(playerlist,CoinList,n)
        return ""
    
    def counter(self, extortion):
        Extortion = False
        if(extortion == False):
            Extortion = True
            print("se bloquea la extorsion")
        return Extortion
    
    def action(self):
        return "steal"
    
