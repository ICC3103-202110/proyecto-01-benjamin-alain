from player import gambler
from assasin import murder
from Duke import Tax
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
from Menu import PlayerMenu
from random import shuffle
from Deck import Deck_cards
from Loser import CardLost
from foreing_aid import Foreing_aid
from coup import COUP
from entry import Entry
from Challenge import duel

class Extend:
    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def  EspecialExt(self,ListPlayer,ingresolog,log,Captain,CAPTAIN,elecction,victimPlayer,point,PersonalDeck,personalCoin,CoinList,unknow,NAMES,SuperHand,n,counters,deck_list):
        while(True):
            while(True):
                #contraataque
                z = 1
                while(z<n):
                    print(z,":",ListPlayer[z])
                    z += 1
                print(n,"nadie quiere contraatacar")
                duelcount = 1
                Challenge = int(input("que jugador desea contratacar? : "))
                print("\n")
                if(Challenge != n): # nadie contraataca se pocede al desafio!!!!!!!!!!!!!!!
                    duelcount = 1
                else:
                    z = 1
                    print("los jugadores que pueden desafiar?: ")
                    while(z<n):
                        print(z,":",ListPlayer[z])
                        z += 1
                    print(n,"nadie quiere desafiar")
                    Challenge = int(input("que jugador desea desafiar? : "))
                    if(Challenge == n):
                        break
                    duelcount = 0    
                if (duelcount == 1): #SI HAY UN CONTRAATAQUE, se ejecuta aca
                    counters = True
                    Reelection = ListPlayer[Challenge]
                    ingresolog = ["el jugador " + ListPlayer[Challenge] + " contraataco al jugador: "+ NAMES]
                    print(ingresolog)
                    log.append(ingresolog)
                    # desafio del contraataque
                    print("quien desea desafiar ?")
                    countChallenge = []
                    pointChallenger = []
                    for contra in range(len(ListPlayer)):
                        #no cuenta el jugador que uso la accion ojo
                        if(ListPlayer[contra] != Reelection):
                            countChallenge.append(ListPlayer[contra]) 
                            pointChallenger.append(point[contra])
                    for i in range(len(countChallenge)):
                        print(i,countChallenge[i])
                    print(i+1,'nadie quiere desafiar')
                    CounterChallenge = int(input("que jugador quiere desafiar al contraataque?: "))
                    if(CounterChallenge != i+1):
                        Ambassator = Exchange("Ambassador")
                        ChallengeCounter = 0
                        ingresolog = ['El jugador: '+countChallenge[CounterChallenge]+' Desafio el contraataque de: '+Reelection]
                        print(ingresolog)
                        log.append(ingresolog)
                        for i in range(len(PersonalDeck[Challenge])):
                            if(PersonalDeck[Challenge][i] == Captain.name or PersonalDeck[Challenge][i] == Ambassator.name):
                                ChallengeCounter += 1
                        if(ChallengeCounter >= 1):
                            ingresolog = ["El jugador: "+Reelection+" Gano el desafio"]
                            log.append(ingresolog)
                            print(ingresolog)
                        else:
                            ingresolog = ["El jugador: "+Reelection+" Pierde el desafio, perdiendo una carta"]
                            #si es que falla aqui se pierde la carta
                            log.append(ingresolog)
                            pointReelec = point[Challenge]
                            pointReelec -= 1
                            point.insert(Challenge,pointReelec)
                            point.pop(Challenge+1)
                            print(ingresolog)
                    ############################
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    personalCoin += 0 
                    CoinList.pop(0)
                    CoinList.insert(0,personalCoin)
                    git = unknow[0]
                    unknow.pop(0)
                    unknow.append(git)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    break

                if (duelcount == 0):  #SI HAY UN DESAFIO, se ejecuta aca
                    duelAmericanCap = 0
                    ingresolog = ["el jugador " + ListPlayer[Challenge] + " desafia al jugador: "+ NAMES+" manteniendo sus monedas"]
                    log.append(ingresolog)
                    print(ingresolog)
                    for i in range(len(SuperHand)): # aqui se verifica la carta
                        if (SuperHand[i] == Captain.name):
                            duelAmericanCap += 1
                    if(duelAmericanCap >= 1):
                        ingresolog = ["El jugador: "+NAMES+" Gano el desafio"]
                        log.append(ingresolog)
                        print(ingresolog)
                        CPoint = point[Challenge]
                        CPoint -= 1
                        point.insert(Challenge,CPoint)
                        point.pop(Challenge+1)
                        counters = False
                    else:
                        ingresolog = ["El jugador: "+NAMES+" Pierde el desafio, perdiendo una carta"]
                        #si es que falla aqui se pierde la carta
                        log.append(ingresolog)
                        playerpoints -= 1
                        point.pop(0)
                        point.append(playerpoints)
                        print(ingresolog)
                        counters = True
                    #print("el jugador " + ListPlayer[Challenge] + " quiere desafiar")
                    #print(ingresolog)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    personalCoin += 0 
                    CoinList.pop(0)
                    CoinList.insert(0,personalCoin)
                    git = unknow[0]
                    unknow.pop(0)
                    unknow.append(git)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    break
                

            if(counters == True):
                CoinList.pop(0)
                CoinList.append(personalCoin)
                ListPlayer.pop(0)
                ListPlayer.append(NAMES)
                PersonalDeck.pop(0)
                PersonalDeck.append(SuperHand)
                git = unknow[0]
                unknow.pop(0)
                unknow.append(git)
                NAMES = ListPlayer[0]
                SuperHand = PersonalDeck[0]
                personalCoin = CoinList[0]
                break
            
            victimCoinss = CoinList[elecction]
            if (victimCoinss < 2):
                victimCoins = CoinList[elecction]-1
            elif(victimCoinss == 0):
                print("no puede robar a esta persona")
                break
            else:
                victimCoins = CoinList[elecction]-2
            ListPlayer.pop(0)
            ListPlayer.append(NAMES)
            PersonalDeck.pop(0)
            PersonalDeck.append(SuperHand)
            personalCoin += 2                  
            CoinList.insert(elecction,victimCoins)
            CoinList.pop(0)
            CoinList.append(personalCoin)
            CoinList.pop(elecction)
            git = unknow[0]
            unknow.pop(0)
            unknow.append(git)
            NAMES = ListPlayer[0]
            SuperHand = PersonalDeck[0]
            personalCoin = CoinList[0]
            shuffle(deck_list)
            break
        return ListPlayer,ingresolog,log,Captain,CAPTAIN,elecction,victimPlayer,point,PersonalDeck,personalCoin,CoinList,unknow,NAMES,SuperHand,n,counters,deck_list