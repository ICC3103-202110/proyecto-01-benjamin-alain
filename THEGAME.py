from player import gambler
from Assasin import murder
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

class Ex:

    def __init__(self,algo):
        self.__algo = algo
    
    @property
    def algo(self):
        return self.__algo
    @algo.setter
    def algo(self,value):
        self.__algo = value
    
        
    def PrincipalGame(self,GlobalList,ListPlayer,PersonalDeck,CoinList,log,unknow,n,deck_list,point):
        PrincipalTurns = 0
        PRINCIPALTIMES = []
        pt = 0
        FirstPlayer = ListPlayer[0]
        while(True):
            if(point[0] <= 0):
                ingresolog = ["El jugador: "+ListPlayer[0]+" a perdido todas sus influencia"]
                log.append(ingresolog)
                print(ingresolog)
                ListPlayer.pop(0)
                PersonalDeck.pop(0)
                CoinList.pop(0)
                point.pop(0)
                unknow.pop(0)
            n = len(ListPlayer)
            if(len(ListPlayer) == 1):
                print("el Ganador es: "+ListPlayer[0]+" ( ͡~ ͜ʖ ͡°)")
                break
            GlobalList = []
            GlobalList.append(ListPlayer)
            GlobalList.append(PersonalDeck)
            GlobalList.append(CoinList)
            #print(GlobalList[0][0])
            NAMES = ListPlayer[0] # nombre del jugador
            #print(ListPlayer)
            SuperHand = PersonalDeck[0] # mano del jugador(cartas que tiene)
            #print(PersonalDeck)
            personalCoin = CoinList[0] # monedas del jugador
            #print(CoinList)
            playerpoints = point[0] # puntos del jugador(influencia)
            print(point)
            print("\n")
            print("le toca a:  ", NAMES, '\nlas influencias que tiene son: ',playerpoints)
            part1 = PlayerMenu(1)
            obj = PlayerMenu(8)
            option1 = part1.menusplayers()
            if(option1 == 1):
                part2 = PlayerMenu(2)
                option2 = part2.menusplayers()
                if(personalCoin >= 10):
                    option2 = 2
                    print('hagas lo que hagas tienes que elegir el golpe (COUP), por tener 10 monedas ')
                while(True):
                    if(option2 == 0):#listo
                        ENTRY = Entry("INGRESO")
                        enter = ENTRY.efect(PrincipalTurns, personalCoin, log, ListPlayer, PersonalDeck, unknow, NAMES, SuperHand, CoinList)
                        PrincipalTurns = enter[0]
                        log = enter[2]
                        ListPlayer = enter[3]
                        PersonalDeck = enter[4]
                        unknow = enter[5]
                        NAMES = enter[6]
                        SuperHand = enter[7]
                        CoinList = enter[8]
                        point.pop(0)
                        point.append(playerpoints)
                        break
                    elif(option2 == 1):#listo
                        Foreign = Foreing_aid("ayuda extranjera").efect(PrincipalTurns, log, personalCoin, NAMES)
                        PrincipalTurns = Foreign[0]
                        log = Foreign[1]
                        personalCoin = Foreign[2]
                        #contraataque
                        while(True):
                            DUKE = Tax("Duque")
                            NewDuke = DUKE.counter(ListPlayer,n)
                            if(NewDuke[2]== n):
                                break
                            count = NewDuke[2]
                            print("el jugador "+ListPlayer[count]+" quiere contratacar")
                            ingresolog = ["el jugador "+ListPlayer[count]+" contraataco al jugador: "+ NAMES+" manteniendo sus monedas"]
                            log.append(ingresolog)
                            # desafio
                            DuelList = []
                            Challenger = duel("foreign_aid",)
                            DUEL = Challenger.dareFA(ListPlayer,CoinList,PersonalDeck,unknow,NAMES,SuperHand,personalCoin,playerpoints,log,count,point)
                            break
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
                        p = point[0]
                        point.pop(0)
                        point.append(p)
                        break
                    elif(option2 == 2 or personalCoin >= 10): #creo que esta listo
                        print("se a seleccionado el golpe\n")
                        if(personalCoin < 7):
                            print("no tienes las monedas suficientes para hacer esta accion")
                            break
                        if(personalCoin >= 10):
                            print("se ha seleccionado el golpe por obligacion")
                        SuperCoup = COUP("Golpe")
                        MegaCoup = SuperCoup.efect(PrincipalTurns, log, personalCoin, CoinList, NAMES, ListPlayer, PersonalDeck, unknow, SuperHand,point, playerpoints,n)
                        break
                    elif(option2 == 3):# creo que esta listo
                        print("se a seleccionado el Impuestos")
                        PrincipalTurns += 1
                        duke = Tax("Duke")
                        DUKE = duke.efect(personalCoin)
                        Gamer = gambler(NAMES,personalCoin,SuperHand,playerpoints).AskMoney(3)
                        personalCoin = Gamer
                        ingresolog = [NAMES +" utiliza la accion "+ duke.action() +" ganado 3 monedas"]
                        log.append(ingresolog)
                        #desafio
                        TaxDuel = duel("DUKE").dare(ListPlayer, CoinList, PersonalDeck, unknow, NAMES, SuperHand, personalCoin, playerpoints, log,n,deck_list,point)
                        personalCoin = TaxDuel[6]
                        print(personalCoin) #algo raro pasa aqui
                        #cambio
                        point.pop()
                        #print(point)
                        point.append(playerpoints)
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
                        break
                    elif(option2 == 4):#lista
                        respaldo = []
                        print("se a seleccionado el Asesinato")
                        x = 1
                        if(personalCoin < 3):
                            print("no tienes monedas suficiente para ejecutar esta accion")
                            break
                        personalCoin -= 3 
                        #print(personalCoin)
                        PrincipalTurns += 1
                        Assassin = murder("Asesino")
                        ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n)  
                        CoinList.pop(0)
                        CoinList.append(personalCoin)
                        elecction = int(input("escoja la victima del asesinato: "))
                        #print(elecction)    
                        MurderVictim = ListPlayer[elecction]
                        ingresolog = [NAMES+" utilizo la accion "+Assassin.action()+" contra "+MurderVictim]
                        log.append(ingresolog)
                        #print(MurderVictim)
                        # desafiar
                        slayer = duel("asesino").dareAC(ListPlayer, ingresolog, NAMES, log, SuperHand, point, x, PersonalDeck, unknow, personalCoin, CoinList,n,MurderVictim)
                        #contraataque
                        murderr = slayer[11]
                        if(murderr == False):
                            y = 1
                            print("quien quiere contraatacar?: ")
                            while(y < len(ListPlayer)):
                                print(y,ListPlayer[y])
                                y += 1
                            print(len(ListPlayer),"nadie quiere contraatacar")
                            MurderDuel = int(input("quien quiere contraatacar?: "))
                            if(MurderDuel != len(ListPlayer)):
                                ingresolog = ["El jugador: "+ListPlayer[MurderDuel]+" Contraataco a: "+NAMES]
                                print(ingresolog)
                                log.append(ingresolog)
                                PointsCounter = point[MurderDuel]
                                print("Quien quiere desafiar el contraataque?: ")
                                y = 1
                                KillerList = []
                                pointkill = []
                                for i in range(len(ListPlayer)):
                                    if(ListPlayer[i] != ListPlayer[MurderDuel] ):
                                        KillerList.append(ListPlayer[i])
                                        pointkill.append(point[i])
                                for kill in range(len(KillerList)):
                                    print(kill,KillerList[kill])
                                print(kill+1,"nadie quiere desafiar el contraataque")
                                CounterKiller = int(input("quien quiere desafiar el contraataque?: "))
                                NameOfDead = KillerList[CounterKiller]
                                if (CounterKiller != kill+1):
                                    CounterMurder = True
                                    CounterCount = 0
                                    ingresolog = ["El jugador: "+KillerList[CounterKiller]+" desafio el contraataque de: "+ListPlayer[MurderDuel]]
                                    log.append(ingresolog)
                                    print(ingresolog)
                                    for i in range(len(PersonalDeck[MurderDuel])):
                                        if(PersonalDeck[MurderDuel][i] == Block.name):
                                            CounterCount += 1
                                    if(CounterCount >= 1):
                                        ingresolog = ["El Jugador: "+ListPlayer[MurderDuel]+" Gana el desafio"]
                                        log.append(ingresolog)
                                        print(ingresolog)
                                        if(MurderVictim == NameOfDead ):
                                            PointsCounter -= 2
                                        else:
                                            PointsCounter -= 1
                                        point.insert(MurderDuel,PointsCounter)
                                    else:
                                        ingresolog = ["El Jugador: "+ListPlayer[MurderDuel]+" pierde el desafio"]
                                        log.append(ingresolog)
                                        print(ingresolog)
                                        murderpoint = pointkill[CounterKiller]
                                        murderpoint -= 2
                                        point.insert(CounterKiller,murderpoint)
                                #print(point)
                                point.pop(n)
                                #print(point)
                                point.append(playerpoints)
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
                            print("solo puede mirar "+MurderVictim)
                            for i in range(len(PersonalDeck[elecction])):
                                print(i,PersonalDeck[elecction][i])
                                respaldo.append(PersonalDeck[elecction][i])
                            victimelection = int(input("jugador, "+MurderVictim+ " elija su carta a eliminar "))
                            SadPointss = point[elecction]
                            SadPointss -= 1
                            point.insert(elecction,SadPointss)
                            point.pop(elecction+1)
                            break
                    elif(option2 == 5):#listo falta consecuencia 
                        #inicio
                        counters = False
                        duelcards = 0
                        print("se a seleccionado la Extorsion")
                        PrincipalTurns += 1
                        Captain = Steal("Capitan")
                        ingresolog = [NAMES + " utilizo la accion " + Captain.action()]
                        log.append(ingresolog)
                        extor = True
                        CAPTAIN = Captain.efect(ListPlayer,1,CoinList,n)
                        print(CAPTAIN)
                        elecction = int(input("escoja la victima del robo: "))
                        victimPlayer = ListPlayer[elecction]
                        ingresolog = [NAMES+", utiliza la accion "+Captain.action()+" para robar monedas a, "+victimPlayer]
                        print(ingresolog)
                        log.append(ingresolog)  
                        print("pero antes quien desea contraatacar? : ")
                        while(True):
                            #contraataque
                            print(ListPlayer)
                            print(1,":",ListPlayer[1])
                            print(2,":",ListPlayer[2])
                            duelcount = 1
                            if(n == 4):
                                print(3,":",ListPlayer[3])
                                print(4,": Nadie quiere contraatacar ")
                                print("\n")
                                count = int(input("que jugador desea contratacar? : "))
                                print("\n")
                                if(count == 4): # nadie contraataca se pocede al desafio!!!!!!!!!!!!!!!
                                    while(True):
                                        print("quien desea desafiar ?")
                                        print(1,":",ListPlayer[1])
                                        print(2,":",ListPlayer[2])
                                        print(3,":",ListPlayer[3])
                                        print(4,":","nadie quiere desafiar")
                                        print("\n")
                                        Challenge = int(input("que jugador desea desafiar? : ")) 
                                        print("\n") 
                                        #nadie de los 4 jugadores quiere desafiar
                                        if(Challenge == 4):
                                            duelcount = 5  
                                            break 
                                        print("el jugador " + ListPlayer[Challenge] + " quiere desafiar")
                                        #ingresolog = ["el jugador " + ListPlayer[Challenge] + "desafia al jugador: "+ NAMES+" manteniendo sus monedas"]
                                        #print(ingresolog)
                                        #log.append(ingresolog)
                                        duelcount = 0
                                        break
                                    if (duelcount == 5):
                                        break
                                    
                            else:
                                print(3,":","nadie quiere contraatacar ")
                                print("\n")
                                count = int(input("Que jugador desea contratacar? :"))
                                print("\n")
                                if(count == 3):
                                    while(True):  #Nadie Contraataca, se procede a DESAFIAR !!!!!!!!!!!!!!!!
                                        print("quien desea desafiar ?")
                                        print(1,":",ListPlayer[1])
                                        print(2,":",ListPlayer[2])
                                        print(3,":","nadie quiere desafiar")
                                        print("\n")
                                        Challenge = int(input("que jugador desea desafiar?: "))
                                        print("\n")
                                        if (Challenge == 3):             #nadie de los 3 jugadores quiere desafiar
                                            duelcount = 5             
                                            break
                                        print("el jugador " + ListPlayer[Challenge] + " quiere desafiar")
                                        ingresolog = ["el jugador " + ListPlayer[Challenge] + " desafia al jugador: "+ NAMES+" manteniendo sus monedas"]
                                        print(ingresolog)
                                        #log.append(ingresolog)
                                        duelcount = 0
                                        counters = False
                                        break
                                    if (duelcount == 5):
                                        break  
                            if (duelcount == 1): #SI HAY UN CONTRAATAQUE, se ejecuta aca
                                counters = True
                                Reelection = ListPlayer[count]
                                print("el jugador " + ListPlayer[count] + " quiere contratacar")
                                ingresolog = ["el jugador " + ListPlayer[count] + " contraataco al jugador: "+ NAMES+" manteniendo sus monedas"]
                                print(ingresolog)
                                log.append(ingresolog)
                                # desafio del contraataque
                                print("quien desea desafiar ?")
                                countChallenge = []
                                for contra in range(len(ListPlayer)):
                                    #no cuenta el jugador que uso la accion ojo
                                    if(ListPlayer[contra] != Reelection):
                                        countChallenge.append(ListPlayer[contra]) 
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
                                    for i in range(len(PersonalDeck[count])):
                                        if(PersonalDeck[count][i] == Captain.name or PersonalDeck[count][i] == Ambassator.name):
                                            ChallengeCounter += 1
                                    if(ChallengeCounter >= 1):
                                        ingresolog = ["El jugador: "+Reelection+" Gano el desafio"]
                                        log.append(ingresolog)
                                        print(ingresolog)
                                    else:
                                        ingresolog = ["El jugador: "+Reelection+" Pierde el desafio, perdiendo una carta"]
                                        #si es que falla aqui se pierde la carta
                                        log.append(ingresolog)

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
                                for i in range(len(SuperHand)): # aqui se verifica la carta
                                    if (SuperHand[i] == Captain.name):
                                        duelAmericanCap += 1
                                if(duelAmericanCap >= 1):
                                    ingresolog = ["El jugador: "+NAMES+" Gano el desafio"]
                                    log.append(ingresolog)
                                    print(ingresolog)
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
                    elif(option2 == 6):#listo 
                        print("se a seleccionado el Cambio")
                        PrincipalTurns += 1
                        Ambassador = Exchange("Ambassador")
                        ingresolog = [NAMES + " utiliza la accion "+Ambassador.action()+" cambiando cartas"]
                        log.append(ingresolog)
                        #desafio
                        Embajator = duel("AMBASSADOR").dare(ListPlayer, CoinList, PersonalDeck, unknow, NAMES, SuperHand, personalCoin, playerpoints, log, n,deck_list,point)
                        break
                        #cambio                           
                    elif(option2 == 7):
                        print("volviendo al menu anterior")
                        break
                    else:
                        print("seleccione un numero valido")
            elif(option1 == 2):#listo
                    print("log general\n")
                    HISTORIAL = PlayerMenu(9).MiniMenu(log)
                    print(HISTORIAL)
                    x = input("presione cualquier tecla para volver")
            elif(option1 == 3):#listo
                q = PlayerMenu(7)
                x = 1
                print(NAMES)
                if(ListPlayer[0] == NAMES):
                    print(q.secondMiniMenu(SuperHand,NAMES,personalCoin))
                    while(x < len(ListPlayer)):
                        print(q.secondMiniMenu(unknow[x],ListPlayer[x],CoinList[x]))
                        x += 1
                    print("cantidad de cartas en el mazo ",len(deck_list))
                    x = input("presione cualquier tecla para volver")
            elif(option1 == 4):
                descripcion = PlayerMenu(6).menusplayers()
                print(descripcion)
                x == (input("presione cualquier tecla para volver"))             
            else:
                print("ingrese un numero valido")