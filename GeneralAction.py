from assasin import murder
from Loser import CardLost
class GENERALEFECT:

    def __init__(self,name,option,PrincipalTurns,log):
        self.__name = name
        self.__option = option
        self.__log = log
        self.__PrincipalTurns = PrincipalTurns
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def option(self):
        return self.__option

    @option.setter
    def option(self,value):
        self.__option = value

    @property
    def log(self):
        return self.__log

    @log.setter
    def log(self,value):
        self.__log = value
    
    @property
    def PrincipalTurns(self):
        return self.__PrincipalTurns

    @PrincipalTurns.setter
    def PrincipalTurns(self,value):
        self.__PrincipalTurns = value

    def COUPEfect(self,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand,point,playerpoints,n):
        self.PrincipalTurns += 1
        respaldo = []
        personalCoin -= 7
        #print(personalCoin)
        Assassin = murder("Asesino")
        CoinList.pop(0)
        CoinList.append(personalCoin)
        ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n,point)  
        elecction = int(input("escoja la victima del asesinato: "))
        #print(elecction)
        while(True):
            try:    
                MurderVictim = ListPlayer[elecction]
                break
            except:
                elecction = int(input("escoja la victima del asesinato: "))
        ingresolog = [NAMES+" utilizo la accion Golpe contra "+MurderVictim]
        self.log.append(ingresolog)
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
        if (n == 4):
            test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,PersonalDeck,n)
        elif(n == 3):
            test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,PersonalDeck,n)
        elif(n == 2):
            test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,PersonalDeck,n)
        return self.PrincipalTurns,self.log,personalCoin,CoinList,NAMES,ListPlayer,PersonalDeck,unknow,SuperHand,point,playerpoints
    def ENTRYEfect(self,personalCoin,ListPlayer,PersonalDeck,unknow,NAMES,SuperHand,CoinList):
        print("se a seleccionado el ingreso")
        self.PrincipalTurns += 1
        print("\n")
        personalCoin += 1
        ingresolog = [NAMES+" obtiene una moneda por ingreso"]
        self.log.append(ingresolog)
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
        return self.PrincipalTurns,personalCoin,self.log,ListPlayer,PersonalDeck,unknow,NAMES,SuperHand,CoinList
    def FOREIGN_AIDEfect(self,personalCoin,NAMES):
        print("se a seleccionado la ayuda extranjera")
        self.PrincipalTurns += 1
        ingresolog = [NAMES+" obtiene 2 moneda por ayuda extranjera"]
        self.log.append(ingresolog)
        personalCoin += 2
        return self.PrincipalTurns,self.log,personalCoin
