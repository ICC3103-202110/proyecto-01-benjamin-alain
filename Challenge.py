from assasin import murder
from Duke import Tax
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
from random import shuffle
from Loser import CardLost
class duel:

    def __init__(self, name,ListPlayer,CoinList,PersonalDeck):
        self.__name = name
        self.__ListPlayer = ListPlayer
        self.__CoinList = CoinList
        self.__PersonalDeck = PersonalDeck
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def ListPlayer(self):
        return self.__ListPlayer

    @ListPlayer.setter
    def ListPlayer(self,value):
        self.__ListPlayer = value
    
    @property
    def CoinList(self):
        return self.__CoinList

    @CoinList.setter
    def CoinList(self,value):
        self.__CoinList = value
    
    @property
    def PersonalDeck(self):
        return self.__PersonalDeck

    @PersonalDeck.setter
    def PersonalDeck(self,value):
        self.__PersonalDeck = value

    def dareAM(self,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point,ver):
        DUKE = Tax("Duke")
        CAPTAIN = Steal("Capitan")
        AMBASSADOR = Exchange("Ambassador")
        CONTESSA = Block("Contessa")
        print("quien quiere desafiar? ")
        if(self.name == AMBASSADOR.name):
            Ambassador = Exchange("Ambassador")
            x = 1
            while(x < n):
                print(x,self.ListPlayer[x])
                x += 1
            print(n,"nadie quiere desafiar")
            MurderDuel = int(input("quien quiere desafiar?: "))
            if(MurderDuel >= n or MurderDuel <= 0):
                MurderDuel = n
            while(True):
                if(MurderDuel == n):
                    AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
                    self.ListPlayer.pop(0)
                    self.ListPlayer.append(NAMES)
                    self.PersonalDeck.pop(0)
                    self.PersonalDeck.append(SuperHand)
                    self.CoinList.pop(0)
                    self.CoinList.append(personalCoin)
                    git = unknow[0]
                    unknow.pop(0)
                    unknow.append(git)
                    NAMES = self.ListPlayer[0]
                    SuperHand = self.PersonalDeck[0]
                    personalCoin = self.CoinList[0]
                    point.pop(0)
                    point.append(playerpoints)
                    shuffle(deck_list)
                    shuffle(deck_list)
                    break
                print("el jugador "+self.ListPlayer[MurderDuel]+" quiere desafiar")
                ingresolog = ["el jugador "+self.ListPlayer[MurderDuel]+" desafiar al jugador: "+ NAMES+" evitando cambiar sus cartas"]
                log.append(ingresolog)
                duelcount = 0
                for duel in range(len(SuperHand)):
                    if(SuperHand[duel] == Ambassador.name):
                        duelcount += 1
                if (duelcount >= 1):
                    ingresolog = [NAMES + " Gana el desafio y utiliza la carta " + Ambassador.name +" "]
                    print(ingresolog)
                    SadResult = point[MurderDuel]
                    SadResult -= 1
                    point.insert(MurderDuel,SadResult)
                    #print(point)
                    point.pop(MurderDuel+1)
                    #print(point)
                    log.append(ingresolog)
                    AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
                    self.ListPlayer.pop(0)
                    self.ListPlayer.append(NAMES)
                    self.PersonalDeck.pop(0)
                    self.PersonalDeck.append(SuperHand)
                    self.CoinList.pop(0)
                    self.CoinList.append(personalCoin)
                    git = unknow[0]
                    unknow.pop(0)
                    unknow.append(git)
                    NAMES = self.ListPlayer[0]
                    SuperHand = self.PersonalDeck[0]
                    personalCoin = self.CoinList[0]
                    point.pop(0)
                    point.append(playerpoints)
                    shuffle(deck_list)
                    shuffle(deck_list)
                    break
                else:
                    ingresolog = [NAMES + " pierde el desafio y pierde una carta"]
                    print(ingresolog)
                    duelerPoints = point[0]
                    duelerPoints -= 1
                    point.append(duelerPoints)
                    #print(point)
                    point.pop(0)
                    #print(point)
                    log.append(ingresolog)
                    self.ListPlayer.pop(0)
                    self.ListPlayer.append(NAMES)
                    self.PersonalDeck.pop(0)
                    self.PersonalDeck.append(SuperHand)
                    self.CoinList.pop(0)
                    self.CoinList.append(personalCoin)
                    git = unknow[0]
                    unknow.pop(0)
                    unknow.append(git)
                    NAMES = self.ListPlayer[0]
                    SuperHand = self.PersonalDeck[0]
                    personalCoin = self.CoinList[0]
                    point.pop(0)
                    point.append(playerpoints)
                    if (n == 4):
                        test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 3):
                        test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 2):
                        test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,self.PersonalDeck,n)
                    shuffle(deck_list)
                    shuffle(deck_list) 
                    break                      
                break
            return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point
    
    def dareFA(self,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,count,point,n):
        print("quien quiere desafiar? ")
        if(self.name == 'foreign_aid'):
            DuelList = []
            for duel in range(len(self.ListPlayer)):
                if(self.ListPlayer[duel] != self.ListPlayer[count]):
                    DuelList.append(self.ListPlayer[duel])
            for LIST in range(len(DuelList)):
                print(LIST,DuelList[LIST])
            print(LIST+1,'nadie quiere desafiar')
            CounterChallenge = int(input("que jugador quiere desafiar al contraataque?: "))
            if(CounterChallenge >= LIST+1 or CounterChallenge < 0):
                CounterChallenge = LIST+1
            if(CounterChallenge != LIST+1):
                HandCounter = self.PersonalDeck[CounterChallenge]
                DUKKE = Tax("Duke")
                ChallengeCounter = 0
                ingresolog = ['El jugador: '+DuelList[CounterChallenge]+' Desafio el contraataque de: '+self.ListPlayer[count]]
                print(ingresolog)
                log.append(ingresolog)
                for i in range(len(self.PersonalDeck[count])):
                    if(self.PersonalDeck[count][i] == DUKKE.name):
                        ChallengeCounter += 1
                if(ChallengeCounter >= 1):
                    ingresolog = ["El jugador: "+self.ListPlayer[count]+" Gano el desafio de "+DuelList[CounterChallenge]]
                    log.append(ingresolog)
                    point[CounterChallenge] -= 1
                    print(ingresolog)
                    point.insert(count,point[CounterChallenge])
                    point.pop()                  
                else:
                    ingresolog = ["El jugador: "+self.ListPlayer[count]+" Pierde el desafio, perdiendo una carta"]
                    #si es que falla aqui se pierde la carta
                    log.append(ingresolog)
                    print(ingresolog)
                    point[count] -= 1
                    print("influencia de ", self.ListPlayer[count],": ",point[count])
                    point.insert(count,point[count])
                    point.pop()
                    if (n == 4):
                        test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 3):
                        test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 2):
                        test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,self.PersonalDeck,n)
                return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   
            else:
                personalCoin -= 2
                return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log   

    def dareAC(self,ingresolog,NAMES,log,SuperHand,point,x,unknow,personalCoin,n,MurderVictim):
        ASSASIN = murder("Asesino")
        print("quien quiere desafiar?: ")
        while(x < n):
            print(x,self.ListPlayer[x])
            x += 1
        print(n,"nadie quiere desafiar")
        MurderDuel = int(input("quien quiere desafiar?: "))
        if(MurderDuel >= n or MurderDuel <= 0):
            MurderDuel = n
        if (MurderDuel != n):
            DuelOfMurder = self.ListPlayer[MurderDuel]
            murderr = True
            CountAssasin = 0
            ingresolog = ['el jugador: '+self.ListPlayer[MurderDuel]+' quire desafiar al jugador: '+NAMES]
            log.append(ingresolog)
            print(ingresolog)
            for i in range(len(SuperHand)):
                if(SuperHand[i] == ASSASIN.name):
                    CountAssasin += 1
            if(CountAssasin >= 1):
                ingresolog = ['El jugador: '+NAMES + ' gana el desafio']
                log.append(ingresolog)
                print(ingresolog)
                dueler = point[MurderDuel]
                if(DuelOfMurder == MurderVictim):
                    dueler -= 2
                    ingresolog = ["al jugador "+DuelOfMurder+" A perdido todas sus influencias de golpe"]
                    log.append(ingresolog)
                else:
                    dueler -= 1
                point.insert(MurderDuel,dueler)
                #point.pop(MurderDuel)
                
            else:
                ingresolog = ['El jugador: '+NAMES+' pierde el desafio']
                log.append(ingresolog)
                print(ingresolog)
                dueler = point[0]
                dueler -= 1
                point.append(dueler)
                #point.pop(0)
            if(murderr == True):
                self.ListPlayer.pop(0)
                self.ListPlayer.append(NAMES)
                self.PersonalDeck.pop(0)
                self.PersonalDeck.append(SuperHand)
                point.pop(0)
                git = unknow[0]
                unknow.pop(0)
                unknow.append(git)
                NAMES = self.ListPlayer[0]
                SuperHand = self.PersonalDeck[0]
                personalCoin = self.CoinList[0]
                return self.ListPlayer,MurderDuel,ingresolog,NAMES,log,SuperHand,point,x,self.PersonalDeck,unknow,personalCoin,murderr
        else:
            murderr = False 
        return self.ListPlayer,MurderDuel,ingresolog,NAMES,log,SuperHand,point,x,self.PersonalDeck,unknow,personalCoin,murderr 

    def dareDU(self,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point,ver):
        DUKE = Tax("Duke")
        CAPTAIN = Steal("Capitan")
        AMBASSADOR = Exchange("Ambassador")
        CONTESSA = Block("Contessa")
        if(self.name == DUKE.name):
            while(True):
                x = 1
                while(x < n):
                    print(x," : ",self.ListPlayer[x])
                    x += 1
                print(x," : ", "nadie quiere desafiar")
                count = int(input("quien desea desafiar?: "))
                if(count >=  x or count <= 0):
                    count = x
                if(count == x):
                    break
                print("el jugador "+self.ListPlayer[count]+" quiere desafiar")
                ver = False
                ingresolog = ["el jugador "+self.ListPlayer[count]+" desafiar al jugador: "+ NAMES+" manteniendo sus monedas"]
                log.append(ingresolog)
                duelcount = 0
                for duel in range(len(SuperHand)):
                    if(SuperHand[duel] == DUKE.name):
                        duelcount += 1
                if (duelcount >= 1):
                    ingresolog = [NAMES + " Gana el desafio y utiliza la carta " + DUKE.name +" ganando 3 monedas"]
                    ver = True
                    print(ingresolog)
                    log.append(ingresolog)
                    Dueler = point[count]
                    Dueler -= 1
                    #print(point)
                    point.insert(count, Dueler)
                    point.pop(count+1)
                    return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point,ver
                else:
                    ingresolog = [NAMES + " pierde el desafio y pierde una carta"]
                    ver = True
                    print(ingresolog)
                    log.append(ingresolog)         
                    personalCoin -= 3   
                    playerpoints -= 1
                    point.append(playerpoints)
                    point.pop(0)
                    #print(point)
                    if (n == 4):
                        test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 3):
                        test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,self.PersonalDeck,n)
                    elif(n == 2):
                        test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,self.PersonalDeck,n)
                    return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point,ver
                break   
            return self.ListPlayer,self.CoinList,self.PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,n,deck_list,point,ver
          