class Foreing_aid:
    
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "Foreing_aid"
        else:
            self.__name = "Foreing_aid"

    def efect(self,PrincipalTurns,log,personalCoin,NAMES):
        print("se a seleccionado la ayuda extranjera")
        PrincipalTurns += 1
        ingresolog = [NAMES+" obtiene 2 moneda por ayuda extranjera"]
        log.append(ingresolog)
        personalCoin += 2
        return PrincipalTurns,log,personalCoin