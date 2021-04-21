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

    def efect(self,PrincipalTurns,log,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand,point,playerpoints,n):
        PrincipalTurns += 1
        respaldo = []
        personalCoin -= 7
        #print(personalCoin)
        Assassin = murder("Asesino")
        CoinList.pop(0)
        CoinList.append(personalCoin)
        ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n,point)  
        elecction = int(input("escoja la victima del asesinato: "))
        #print(elecction)    
        MurderVictim = ListPlayer[elecction]
        ingresolog = [NAMES+" utilizo la accion Golpe contra "+MurderVictim]
        log.append(ingresolog)
        #print(MurderVictim)
        print("solo puede mirar "+MurderVictim)
        for i in range(len(PersonalDeck[elecction])):
            print(i,PersonalDeck[elecction][i])
            respaldo.append(PersonalDeck[elecction][i])
        victimelection = int(input("jugador, "+MurderVictim+ " elija su carta a eliminar ")) 
        SadPoint = point[elecction]
        SadPoint -= 1
        point.insert(elecction,SadPoint)
        point.pop(elecction+1)
        u = unknow[0]
        unknow.pop(0)
        unknow.append(u)
        ListPlayer.pop(0)
        ListPlayer.append(NAMES)
        PersonalDeck.pop(0)
        PersonalDeck.append(SuperHand)
        point.pop(0)
        point.append(playerpoints)
        return PrincipalTurns,log,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand,point,playerpoints
                        
                        
        