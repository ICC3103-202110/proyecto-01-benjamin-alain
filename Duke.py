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
    
    def counter(self):
        #el counter es bloquear ayuda extranjera
        return 0
    
    def action(self):
        return "taxes"
