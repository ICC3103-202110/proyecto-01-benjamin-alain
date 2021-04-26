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
from Challenge import duel
from ExtendExtortion import Extend
from GeneralAction import GENERALEFECT


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
            reset = 0
            while(reset <len(ListPlayer)):
                if(point[reset] <= 0):
                    ingresolog = ["El jugador: "+ListPlayer[reset]+" a perdido todas sus influencia"]
                    log.append(ingresolog)
                    print(ingresolog)
                    ListPlayer.pop(reset)
                    PersonalDeck.pop(reset)
                    CoinList.pop(reset)
                    point.pop(reset)
                    unknow.pop(reset)
                    reset += 1
                reset += 1
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
            for i in range(len(ListPlayer)):
                print("--> Jugador: "+ListPlayer[i]+"| Monedas: "+str(CoinList[i])+"| cantidad de influencias actuales: "+str(point[i]))
            print("\n")
            print("le toca a:  ", NAMES, '\nlas influencias que tiene son: ',playerpoints)
            print("\n")
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
                        ENTRY = GENERALEFECT("INGRESO",1,PrincipalTurns, log)
                        entry = ENTRY.ENTRYEfect(personalCoin, ListPlayer, PersonalDeck, unknow, NAMES, SuperHand, CoinList)
                        point.pop(0)
                        point.append(playerpoints)
                        break
                    elif(option2 == 1):#listo
                        Foreign = GENERALEFECT("AYUDA EXTRANJERA",2,PrincipalTurns, log).FOREIGN_AIDEfect(personalCoin, NAMES)
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
                            ingresolog = ["el jugador "+ListPlayer[count]+" contraataco al jugador: "+ NAMES+" "]
                            log.append(ingresolog)
                            # desafio
                            DuelList = []
                            Challenger = duel("foreign_aid",ListPlayer, CoinList, PersonalDeck)
                            DUEL = Challenger.dareFA(unknow, NAMES, SuperHand, personalCoin, playerpoints, log, count, point, n)
                            break
                        try:
                            personalCoin = DUEL[6]
                        except:
                            personalCoin += 0
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
                        point.pop(0)
                        point.append(playerpoints)
                        break
                    elif(option2 == 2 or personalCoin >= 10): # listo
                        print("se a seleccionado el golpe\n")
                        if(personalCoin < 7):
                            print("no tienes las monedas suficientes para hacer esta accion")
                            break
                        if(personalCoin >= 10):
                            print("se ha seleccionado el golpe por obligacion")
                        SuperCoup = GENERALEFECT("GOLPE",3,PrincipalTurns, log)
                        MegaCoup = SuperCoup.COUPEfect(personalCoin, CoinList, NAMES, ListPlayer, PersonalDeck, unknow, SuperHand, point, playerpoints, n)
                        break
                    elif(option2 == 3):#listo
                        print("se a seleccionado el Impuestos")
                        ver = True
                        PrincipalTurns += 1
                        Gamer = gambler(NAMES,personalCoin,SuperHand,playerpoints).AskMoney(3)
                        personalCoin = Gamer
                        duke = Tax("Duke")
                        ingresolog = [NAMES +" utiliza la accion "+ duke.action() +" ganado 3 monedas"]
                        log.append(ingresolog)
                        #desafio
                        '''
                        TaxDuel = duel("DUKE").dare(ListPlayer, CoinList, PersonalDeck, unknow, NAMES, SuperHand, personalCoin, playerpoints, log,n,deck_list,point, ver)
                        '''
                        TaxDuel = duel("DUKE",ListPlayer, CoinList, PersonalDeck).dareDU(unknow, NAMES, SuperHand, personalCoin, playerpoints, log, n, deck_list, point, ver)
                        personalCoin = TaxDuel[6]
                         #algo raro pasa aqui
                        #cambio
                        #print(point)
                        Validate = TaxDuel[11]
                        if(Validate == True):
                            pass
                        else:
                            point.append(playerpoints)
                            point.pop(0)
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
                        ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n,point)  
                        CoinList.pop(0)
                        CoinList.append(personalCoin)
                        elecction = int(input("escoja la victima del asesinato: "))
                        #print(elecction)    
                        while(True):
                            try:
                                MurderVictim = ListPlayer[elecction]
                                break
                            except:
                                elecction = int(input("escoja la victima del asesinato: "))
                        ingresolog = [NAMES+" utilizo la accion "+Assassin.action()+" contra "+MurderVictim]
                        log.append(ingresolog)
                        #print(MurderVictim)
                        # desafiar
                        slayer = duel("asesino",ListPlayer, CoinList, PersonalDeck).dareAC(ingresolog, NAMES, log, SuperHand, point, x, unknow, personalCoin, n, MurderVictim)
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
                            if(MurderDuel >=  len(ListPlayer) or MurderDuel <= 0 ):
                                MurderDuel = len(ListPlayer)
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
                                if(CounterKiller >= kill+1 or CounterKiller < 0):
                                    CounterKiller =  kill+1
                                if (CounterKiller != kill+1):
                                    NameOfDead = KillerList[CounterKiller]
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
                                        point.pop(CounterKiller+1)
                                        print(ListPlayer)
                                        if (n == 4):
                                            test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,PersonalDeck,n)
                                        elif(n == 3):
                                            test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,PersonalDeck,n)
                                        elif(n == 2):
                                            test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,PersonalDeck,n)
                                        break
                                else:
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
                                    point.pop(0)
                                    point.append(playerpoints)
                                    break
                                #print(point)
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
                                point.pop(0)
                                point.append(playerpoints)
                                break
                            print("solo puede mirar "+MurderVictim)
                            for i in range(len(PersonalDeck[elecction])):
                                print(i,PersonalDeck[elecction][i])
                                respaldo.append(PersonalDeck[elecction][i])
                            victimelection = int(input("jugador, "+MurderVictim+ " elija su carta a eliminar "))
                            SadPointss = point[elecction]
                            SadPointss -= 1
                            point.insert(elecction,SadPointss)
                            point.pop(elecction+1)
                            point.pop(0)
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
                            if (n == 4):
                                test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,PersonalDeck,n)
                            elif(n == 3):
                                test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,PersonalDeck,n)
                            elif(n == 2):
                                test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,PersonalDeck,n)
                            break
                    elif(option2 == 5):#listo
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
                        elecction = int(input("escoja la victima del robo: "))
                        while(True):
                            try:
                                victimPlayer = ListPlayer[elecction]
                                break
                            except:
                                elecction = int(input("escoja la victima del robo: "))
                        if(elecction == 0):
                            print("no se puede robar a si mismo")
                            break
                        victimCoinss = CoinList[elecction]
                        if(victimCoinss == 0):
                            print("no puede robar a esta persona")
                            ingresolog = ["el jugador: "+NAMES +" no pudo robar al jugador: "+ListPlayer[elecction]+ " no tiene suficientes monedas"]
                            log.append(ingresolog)
                            break
                        if (victimCoinss < 2):
                            victimCoins = CoinList[elecction]-1
                        else:
                            victimCoins = CoinList[elecction]-2
                        ingresolog = [NAMES+", utiliza la accion "+Captain.action()+" para robar monedas a, "+victimPlayer]
                        print(ingresolog)
                        log.append(ingresolog)  
                        print("pero antes quien desea contraatacar? : ")
                        while(True):
                        
                            #contraataque
                            z = 1
                            while(z<n):
                                print(z,":",ListPlayer[z])
                                z += 1
                            print(n,"nadie quiere contraatacar")
                            duelcount = 1
                            Challenge = int(input("que jugador desea contratacar? : "))
                            if(Challenge >= n or Challenge <= 0):
                                Challenge = n
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
                                if(Challenge >= n or Challenge <= 0):
                                    Challenge = n 
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
                                if(CounterChallenge >= i+1 or CounterChallenge < 0):
                                    CounterChallenge = i+1
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
                                        pointChallenger[CounterChallenge] -= 1
                                        point.insert(CounterChallenge,pointChallenger[CounterChallenge])
                                        point.pop(Challenge+1)
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
                                ingresolog = ["el jugador " + ListPlayer[Challenge] + " desafia al jugador: "+ NAMES+" "]
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
                                    if (n == 4):
                                        test = CardLost("r").DropCard_2_n_4(SuperHand,unknow,point,PersonalDeck,n)
                                    elif(n == 3):
                                        test = CardLost("r").DropCard_2_n_3(SuperHand,unknow,point,PersonalDeck,n)
                                    elif(n == 2):
                                        test = CardLost("r").DropCard_2_n_2(SuperHand,unknow,point,PersonalDeck,n)
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
                        ver = True
                        PrincipalTurns += 1
                        Ambassador = Exchange("Ambassador")
                        ingresolog = [NAMES + " utiliza la accion "+Ambassador.action()+" cambiando cartas"]
                        log.append(ingresolog)
                        #desafio
                        Embajator = duel("AMBASSADOR", ListPlayer, CoinList, PersonalDeck).dareAM(unknow, NAMES, SuperHand, personalCoin, playerpoints, log, n, deck_list, point, ver)
                        break                        
                    elif(option2 == 7):
                        print("volviendo al menu anterior")
                        break
                    else:
                        print("seleccione un numero valido")
                        print("se volvera al menu anterior")
                        break
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
                x = (input("presione cualquier tecla para volver"))             
            else:
                print("ingrese un numero valido")