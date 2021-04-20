from Assasin import murder

class COUP:

    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "coup"
        else:
            self.__name = "coup"

    def efect(self,PrincipalTurns,log,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand):
        print("se a seleccionado el golpe\n")
        if(personalCoin < 7):
            print("no tienes las monedas suficientes para hacer esta accion")
        if(personalCoin >= 10):
            print("se ha seleccionado el golpe por obligacion")
        PrincipalTurns += 1
        respaldo = []
        personalCoin -= 7
        #print(personalCoin)
        Assassin = murder("Asesino")
        CoinList.pop(0)
        CoinList.append(personalCoin)
        ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n)  
        elecction = int(input("escoja la victima del asesinato: "))
        #print(elecction)    
        MurderVictim = ListPlayer[elecction]
        ingresolog = [NAMES+"utilizo la accion Golpe contra "+MurderVictim]
        log.append(ingresolog)
        #print(MurderVictim)
        print("solo puede mirar "+MurderVictim)
        for i in range(len(PersonalDeck[elecction])):
            print(i,PersonalDeck[elecction][i])
            respaldo.append(PersonalDeck[elecction][i])
        victimelection = int(input("jugador, "+MurderVictim+ " elija su carta a eliminar ")) 
        respaldo2 = respaldo[victimelection]    
        var = (remplazo(respaldo2))
        unknow.pop(elecction)
        #print(unknow)
        unknow.insert(elecction,var)
        #print(unknow)
        unknow.pop(0)
        #print(unknow)
        #unknow.append(remplazo("??"))
        #print(unknow)
        ListPlayer.pop(0)
        print(ListPlayer)
        ListPlayer.append(NAMES)
        print(ListPlayer)
        PersonalDeck.pop(0)
        print(PersonalDeck)
        PersonalDeck.append(SuperHand)
        print(PersonalDeck)
        return PrincipalTurns,log,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand
                        
                        
        