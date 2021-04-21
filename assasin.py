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
    
    def efect(self, playerlist,CoinList, cards,n,point):
        L = []
        x = 0
        while(x<len(playerlist)):
            fila = [str(x)+". Jugador: "+playerlist[x]+"| influencias: "+str(point[x])]
            L.append(fila)
            x += 1
        L.pop(0)
        for i in range(len(L)):
            print(L[i]) 
        return ""
        
    def counter(self):
        pass
    
    def action(self):
        return "assassinate"