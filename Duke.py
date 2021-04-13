from IEespecial import IEspecialAtack

class Tax(IEspecialAtack):

    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "DUKE"
        else:
            self.__name = value
    
    def efect(self,coins):
        x = coins + 3
        return x
    
    def counter(self,foreign_aid):
        #el counter es bloquear ayuda extranjera
        if(foreign_aid == True):
            foreign_aid = False
        print("se bloquea la ayuda externa")
        return foreign_aid
    
    def action(self):
        return "taxes"
