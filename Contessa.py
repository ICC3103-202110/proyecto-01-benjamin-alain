from IEespecial import IEspecialAtack

class Block(IEspecialAtack):

    def __init__(self, name):
        self.__name = name
           
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "Contessa"
        else:
            self.__name = "Contessa"
    
    def efect(self):
        pass
    
    def counter(self, Assessination):
        if(Assessination == True):
            Assessination = False
        print("se bloquea Assessination")
        return Assessination
    
    def action(self):
        pass