from IEespecial import IEspecialAtack

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
    
    def efect(self, playerlist, extorsion):
        def ShowPlayers(playerlist):
            print("actual player in the game")
            for (i, _) in enumerate(playerlist):
                print(i+1,") nombre: ",playerlist[i].name,"| card: ",playerlist[i].cards)
        ShowPlayers(playerlist)
        if(extorsion == True):
            y = int(input("seleccione al jugador que quiera quitar monedas"))
            return y
        else:
            y = "se ha bloqueado la extorsion"
            return y
    
    def counter(self, extorsion):
        if(extorsion == True):
            extorsion = False
        print("se bloquea la extorsion")
        return extorsion
    
    def action(self):
        return "steal"