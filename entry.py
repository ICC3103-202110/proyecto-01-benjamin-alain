class Entry:
    
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "entry"
        else:
            self.__name = "entry"
    
    def efect(self,PrincipalTurns,personalCoin,log,ListPlayer,PersonalDeck,unknow,NAMES,SuperHand,CoinList):
        print("se a seleccionado el ingreso")
        PrincipalTurns += 1
        print("\n")
        personalCoin += 1
        ingresolog = [NAMES+" obtiene una moneda por ingreso"]
        log.append(ingresolog)
        ListPlayer.pop(0)
        ListPlayer.append(NAMES)
        PersonalDeck.pop(0)
        PersonalDeck.append(SuperHand)
        CoinList.pop(0)
        CoinList.append(personalCoin)
        git = unknow[0]
        unknow.pop(0)
        unknow.append(git)
        NAMES = ListPlayer[0]
        SuperHand = PersonalDeck[0]
        personalCoin = CoinList[0]
        return PrincipalTurns,personalCoin,log,ListPlayer,PersonalDeck,unknow,NAMES,SuperHand,CoinList