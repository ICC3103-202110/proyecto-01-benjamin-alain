from Assasin import murder
from Duke import Tax
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
from random import shuffle

class duel:

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    def dare(self,ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list):
        ASSASIN = murder("Asesino")
        DUKE = Tax("Duke")
        CAPTAIN = Steal("Capitan")
        AMBASSADOR = Exchange("Ambassador")
        CONTESSA = Block("Contessa")
        print("quien quiere desafiar? ")
        print(AMBASSADOR.name)
        if(self.name == AMBASSADOR.name):
            Ambassador = Exchange("Ambassador")
            while(True):
                print(1,ListPlayer[1])
                print(2,ListPlayer[2])
                if(n == 4):
                    print(3,ListPlayer[3])
                    print(4,"nadie quiere desafiar: ")
                    count = int(input("que jugador desea desafiar: "))
                    if(count == 4):
                        AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
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
                        shuffle(deck_list)
                        shuffle(deck_list)
                        break
                else:
                    print(3,"nadie quiere desafiar: ")
                    count = int(input("que jugador desea desafiar: "))
                    if(count == 3):
                        AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
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
                        shuffle(deck_list)
                        shuffle(deck_list)
                        break
                print("el jugador "+ListPlayer[count]+" quiere desafiar")
                ingresolog = ["el jugador "+ListPlayer[count]+" desafiar al jugador: "+ NAMES+" evitando cambiar sus cartas"]
                log.append(ingresolog)
                duelcount = 0
                for duel in range(len(SuperHand)):
                    if(SuperHand[duel] == Ambassador.name):
                        duelcount += 1
                if (duelcount >= 1):
                    ingresolog = [NAMES + " Gana el desafio y utiliza la carta " + Ambassador.name +" "]
                    print(ingresolog)
                    log.append(ingresolog)
                    AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
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
                    shuffle(deck_list)
                    shuffle(deck_list)
                    break
                else:
                    ingresolog = [NAMES + " pierde el desafio y pierde una carta"]
                    print(ingresolog)
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
                    shuffle(deck_list)
                    shuffle(deck_list) 
                    break                      
                break
            return ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log
        if(self.name == DUKE.name):
            print(DUKE.name)
            while(True):
                print(1,":",ListPlayer[1])
                print(2,":",ListPlayer[2])
                if(n == 4):
                    print(3,":",ListPlayer[3])
                    print(4,":","nadie quiere desafiar ")
                    print("\n")
                    count = int(input("que jugador desea desafiar? : "))
                    if(count == 4):
                        break
                else:
                    print(3,":","nadie quiere desafiar ")
                    print("\n")
                    count = int(input("que jugador desea desafiar? : "))
                    if(count == 3):
                        break
                print("el jugador "+ListPlayer[count]+" quiere desafiar")
                ingresolog = ["el jugador "+ListPlayer[count]+" desafiar al jugador: "+ NAMES+" manteniendo sus monedas"]
                log.append(ingresolog)
                duelcount = 0
                for duel in range(len(SuperHand)):
                    if(SuperHand[duel] == DUKE.name):
                        duelcount += 1
                if (duelcount >= 1):
                    ingresolog = [NAMES + " Gana el desafio y utiliza la carta " + DUKE.name +" ganando 3 monedas"]
                    print(ingresolog)
                    log.append(ingresolog)
                    return ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   
                else:
                    ingresolog = [NAMES + " pierde el desafio y pierde una carta"]
                    print(ingresolog)
                    log.append(ingresolog)
                    print(unknow)          
                    personalCoin -= 3   
                    print(personalCoin)
                    return ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   
                break   
            return ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   
    
    def dareFA(self,ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,count,point):
        print("quien quiere desafiar? ")
        if(self.name == 'foreign_aid'):
            DuelList = []
            for duel in range(len(ListPlayer)):
                if(ListPlayer[duel] != ListPlayer[count]):
                    DuelList.append(ListPlayer[duel])
            for LIST in range(len(DuelList)):
                print(LIST,DuelList[LIST])
            print(LIST+1,'nadie quiere desafiar')
            CounterChallenge = int(input("que jugador quiere desafiar al contraataque?: "))
            if(CounterChallenge != LIST+1):
                DUKKE = Tax("Duke")
                ChallengeCounter = 0
                ingresolog = ['El jugador: '+DuelList[CounterChallenge]+' Desafio el contraataque de: '+ListPlayer[count]]
                print(ingresolog)
                log.append(ingresolog)
                for i in range(len(PersonalDeck[count])):
                    if(PersonalDeck[count][i] == DUKKE.name):
                        ChallengeCounter += 1
                if(ChallengeCounter >= 1):
                    ingresolog = ["El jugador: "+ListPlayer[count]+" Gano el desafio de "+DuelList[CounterChallenge]]
                    log.append(ingresolog)
                    point[CounterChallenge] -= 1
                    print(ingresolog)
                    point.insert(count,point[CounterChallenge])
                    point.pop()
                    print(point)                        
                else:
                    ingresolog = ["El jugador: "+ListPlayer[count]+" Pierde el desafio, perdiendo una carta"]
                    #si es que falla aqui se pierde la carta
                    log.append(ingresolog)
                    print(ingresolog)
                    point[count] -= 1
                    print("influencia de ", ListPlayer[count],": ",point[count])
                    point.insert(count,point[count])
                    point.pop()
                    print(point)
                return ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   
                    