from Winner import Won
from player import gambler
from Assasin import murder
from Duke import Tax
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
from Menu import PlayerMenu
from random import shuffle
from Deck import Deck_cards
from Extra import Ex

playerlist = []
deck = []
player1 = []
player2 = []
player3 = []
player4 = []
JAND1 = []
JAND2 = []
JAND3 = []
JAND4 = []
ALLDeck = []

def MoneyLess(coin,n):
    newcoins = coin-n
    return newcoins

def remplazo(CardName):
    unknow2 = ["??",CardName]
    return unknow2

'''
def remplazo(CardName,NameCard): # seria poner el NameCard como ?? y cuanto 
    unknow2 = [NameCard,CardName]
    return unknow2

'''

def CreatePlayer1(n, hand):
    x = 1
    while (x<=n):
        name = input("your name: ")
        coin = 2
        card = hand[x-1]
        playerlist.append(gambler(name,coin,card))
        x += 1
    return playerlist


def Game(n):
    l=[]
    ListPlayer = []
    deck_list=[]
    PersonalDeck = []
    CoinList = []
    incognita = ["??","??"]
    objeto=Deck_cards("Name_card_object")
    x = objeto.first_round(l)

    handplayer1 = objeto.hand(player1,x)
    handplayer2 = objeto.hand(player2, handplayer1[1])
    handplayer3 = objeto.hand(player3, handplayer2[1])
    if(n == 4):
        handplayer4 = objeto.hand(player4, handplayer3[1])
    for i in range(len(handplayer3[0])):
        JAND1.append(handplayer1[0][i].name)
        JAND2.append(handplayer2[0][i].name)
        JAND3.append(handplayer3[0][i].name)
        if(n == 4):
            JAND4.append(handplayer4[0][i].name)
    if(n == 3):
        for i in range(len(handplayer3[1])):
            deck_list.append(handplayer3[1][i].name) #son las cartas del mazo
    elif(n == 4):
        for i in range(len(handplayer4[1])):
            deck_list.append(handplayer4[1][i].name)
    ALLDeck.append(JAND1)
    ALLDeck.append(JAND2)
    ALLDeck.append(JAND3)
    if(n == 4):
        ALLDeck.append(JAND4)
    List = CreatePlayer1(n,ALLDeck)  
    PersonalDeck = ALLDeck
    for i in range(len(List)):
        ListPlayer.append(List[i].name)
        CoinList.append(List[i].coins)
    unknow = []
    #print(PersonalDeck)
    for i in range(len(PersonalDeck)):
        unknow.append(incognita)
    #print(unknow)
    LOG = []
    log = []
    GlobalList3 = []
    GlobalList4 = []
    turns = 0
    GlobalTurns = 0
    GlobalList3.append(ListPlayer)
    GlobalList3.append(PersonalDeck)
    GlobalList3.append(CoinList)
    log.append("turno numero: "+str(turns))
    #TheGame = Ex("princiapl").principalGame(GlobalList3,ListPlayer,PersonalDeck,CoinList,log,unknow,n,deck_list)
    #print(TheGame)
    while(True):
        GlobalList = []
        GlobalList.append(ListPlayer)
        GlobalList.append(PersonalDeck)
        GlobalList.append(CoinList)
        print(GlobalList[0][0])
        NAMES = ListPlayer[0]
        #print(ListPlayer)
        SuperHand = PersonalDeck[0]
        #print(PersonalDeck)
        personalCoin = CoinList[0]
        #print(CoinList)
        print("\n")
        print("le toca a:  ", NAMES)
        part1 = PlayerMenu(1)
        obj = PlayerMenu(8)
        option1 = part1.menusplayers()
        if(option1 == 1):
            part2 = PlayerMenu(2)
            option2 = part2.menusplayers()
            while(True):
                if(option2 == 0):#listo
                    print("se a seleccionado el ingreso")
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
                    print()
                    break
                elif(option2 == 1):#falta desfio del contraataque
                    print("se a seleccionado la ayuda extranjera")
                    ingresolog = [NAMES+" obtiene 2 moneda por ayuda extranjera"]
                    log.append(ingresolog)
                    personalCoin += 2
                    while(True):
                        print(1,ListPlayer[1])
                        print(2,ListPlayer[2])
                        if(n == 4):
                            print(3,ListPlayer[3])
                            print(4,"nadie quiere contraatacar: ")
                            count = int(input("que jugador desea contratacar: "))
                            if(count == 4):
                                break
                        else:
                            print(3,"nadie quiere contraatacar: ")
                            count = int(input("que jugador desea contratacar: "))
                            if(count == 3):
                                break
                        print("el jugador "+ListPlayer[count]+" quiere contratacar")
                        ingresolog = ["el jugador "+ListPlayer[count]+" contraataco al jugador: "+ NAMES+" manteniendo sus monedas"]
                        log.append(ingresolog)
                        #ListPlayer.pop(0)
                        #ListPlayer.append(NAMES)
                        PersonalDeck.pop(0)
                        print("personalCoin",personalCoin)
                        PersonalDeck.append(SuperHand)
                        print(PersonalDeck)
                        personalCoin = personalCoin-2 
                        print("personalCoin",personalCoin)
                        CoinList.pop(0)
                        print("Coinlist",CoinList)
                        CoinList.insert(0,personalCoin)
                        print("Coinlist",CoinList)
                        git = unknow[0]
                        unknow.pop(0)
                        unknow.append(git)
                        NAMES = ListPlayer[0]
                        SuperHand = PersonalDeck[0]
                        personalCoin = CoinList[0]
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
                    break
                elif(option2 == 2 or personalCoin >= 10):
                    #terminar esto
                    print("se a seleccionado el golpe\n")
                    if(personalCoin < 7):
                        print("no tienes las monedas suficientes para hacer esta accion")
                        break
                    if(personalCoin >= 10):
                        print("se ha seleccionado el golpe por obligacion")
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
                    print(unknow)
                    unknow.insert(elecction,var)
                    print(unknow)
                    unknow.pop(0)
                    print(unknow)
                    unknow.append(remplazo("??"))
                    print(unknow)
                    ListPlayer.pop(0)
                    print(ListPlayer)
                    ListPlayer.append(NAMES)
                    print(ListPlayer)
                    PersonalDeck.pop(0)
                    print(PersonalDeck)
                    PersonalDeck.append(SuperHand)
                    print(PersonalDeck)
                    break
                elif(option2 == 3):#listo falta consecuencia
                    #seleccion
                    print("se a seleccionado el Impuestos")
                    duke = Tax("Duke")
                    DUKE = duke.efect(personalCoin)
                    personalCoin = DUKE
                    ingresolog = [NAMES +" utiliza la accion "+ duke.action() +" ganado 3 monedas"]
                    log.append(ingresolog)
                    #desafio
                    print("quien quiere desafiar? ")
                    while(True):
                        print(1,ListPlayer[1])
                        print(2,ListPlayer[2])
                        if(n == 4):
                            print(3,ListPlayer[3])
                            print(4,"nadie quiere desafiar: ")
                            count = int(input("que jugador desea desafiar: "))
                            if(count == 4):
                                break
                        else:
                            print(3,"nadie quiere desafiar: ")
                            count = int(input("que jugador desea desafiar: "))
                            if(count == 3):
                                break
                        print("el jugador "+ListPlayer[count]+" quiere desafiar")
                        ingresolog = ["el jugador "+ListPlayer[count]+" desafiar al jugador: "+ NAMES+" manteniendo sus monedas"]
                        log.append(ingresolog)
                        duelcount = 0
                        for duel in range(len(SuperHand)):
                            if(SuperHand[duel] == duke.name):
                                duelcount += 1
                        if (duelcount >= 1):
                            ingresolog = [NAMES + " Gana el desafio y utiliza la carta " + duke.name +" ganando 3 monedas"]
                            print(ingresolog)
                            log.append(ingresolog)
                        else:
                            ingresolog = [NAMES + " pierde el desafio y pierde una carta"]
                            print(ingresolog)
                            log.append(ingresolog)          
                            personalCoin -= 3                  
                        break
                    #cambio
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
                elif(option2 == 4):
                    respaldo = []
                    print("se a seleccionado el Asesinato")
                    if(personalCoin < 3):
                        print("no tienes monedas suficiente para ejecutar esta accion")
                        break
                    personalCoin -= 3 
                    #print(personalCoin)
                    Assassin = murder("Asesino")
                    ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n)  
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
                    elecction = int(input("escoja la victima del asesinato: "))
                    #print(elecction)    
                    MurderVictim = ListPlayer[elecction]
                    ingresolog = [NAMES+"utilizo la accion"+Assassin.action()+"contra "+MurderVictim]
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
                    print(unknow)
                    unknow.insert(elecction,var)
                    print(unknow)
                    unknow.pop(0)
                    print(unknow)
                    unknow.append(remplazo("??"))
                    print(unknow)
                    ListPlayer.pop(0)
                    print(ListPlayer)
                    ListPlayer.append(NAMES)
                    print(ListPlayer)
                    PersonalDeck.pop(0)
                    print(PersonalDeck)
                    PersonalDeck.append(SuperHand)
                    print(PersonalDeck)
                    break
                elif(option2 == 5):#falta desafio del contraataque
                    #inicio
                    counters = False
                    duelcards = 0
                    print("se a seleccionado la Extorsion")
                    Captain = Steal("Capitan")
                    ingresolog = [NAMES + " utilizo la accion " + Captain.action()]
                    log.append(ingresolog)
                    extor = True
                    CAPTAIN = Captain.efect(ListPlayer,1,CoinList,n)
                    print(CAPTAIN)
                    elecction = int(input("escoja la victima del robo: "))
                    print("pero antes quien desea contraatacar?: ")
                    while(True):
                        #contraataque
                        print(1,ListPlayer[1])
                        print(2,ListPlayer[2])
                        duelcount = 1
                        if(n == 4):
                            print(3,ListPlayer[3])
                            print(4,"nadie quiere contraatacar: ")
                            count = int(input("que jugador desea contratacar: "))
                            if(count == 4): # nadie contraataca se pocede al desafio!!!!!!!!!!!!!!!
                                while(True):
                                    print("quien desea desafiar ?")
                                    print(1,ListPlayer[1])
                                    print(2,ListPlayer[2])
                                    print(3,ListPlayer[3])
                                    print(4,"nadie quiere desafiar")
                                    Challenge = int(input("que jugador desea desafiar?: "))  
                                    #nadie de los 4 jugadores quiere desafiar
                                    if(Challenge == 4):
                                        duelcount = 5  
                                        break 
                                    print("el jugador quiere desafiar")
                                    #ingresolog = ["el jugador " + ListPlayer[Challenge] + "desafia al jugador: "+ NAMES+" manteniendo sus monedas"]
                                    #print(ingresolog)
                                    #log.append(ingresolog)
                                    duelcount = 0
                                    break
                                if (duelcount == 5):
                                    break
                                
                        else:
                            print(3,"nadie quiere contraatacar: ")
                            count = int(input("que jugador desea contratacar: "))
                            if(count == 3):
                                while(True):  #Nadie Contraataca, se procede a DESAFIAR !!!!!!!!!!!!!!!!
                                    print("quien desea desafiar ?")
                                    print(1,ListPlayer[1])
                                    print(2,ListPlayer[2])
                                    print(3,"nadie quiere desafiar")
                                    Challenge = int(input("que jugador desea desafiar?: "))
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
                            print("el jugador " + ListPlayer[elecction] + " quiere contratacar")
                            ingresolog = ["el jugador " + ListPlayer[elecction] + " contraataco al jugador: "+ NAMES+" manteniendo sus monedas"]
                            print(ingresolog)
                            print("SI HAY UN CONTRAATAQUE, se ejecuta aca")
                            print("quien desea desafiar ?")
                            print(ListPlayer[elecction])
                            print(1,ListPlayer[0])
                            print(2,ListPlayer[2])
                            print(3,"nadie quiere desafiar")
                            log.append(ingresolog)
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
                                print(ingresolog)
                                counters = True
                            #print("el jugador " + ListPlayer[Challenge] + " quiere desafiar")
                            #print(ingresolog)
                            print("SI HAY UN DESAFIO, se ejecuta aca")
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
                        
                    victimPlayer = ListPlayer[elecction]
                    victimCoinss = CoinList[elecction]
                    if (victimCoinss < 2):
                        victimCoins = CoinList[elecction]-1
                    elif(victimCoinss == 0):
                        print("no puede robar a esta persona")
                        break
                    else:
                        victimCoins = CoinList[elecction]-2
                    ingresolog = [NAMES+", utiliza la accion "+Captain.action()+" para robar monedas a, "+victimPlayer]
                    print(ingresolog)
                    log.append(ingresolog)
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
                elif(option2 == 6):#listo falta consecuencia
                    print("se a seleccionado el Cambio")
                    Ambassador = Exchange("Ambassador")
                    ingresolog = [NAMES + " utiliza la accion "+Ambassador.action()+" cambiando cartas"]
                    log.append(ingresolog)
                    #desafio
                    print("quien quiere desafiar? ")
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
                    break
                    #cambio                           
                elif(option2 == 7):
                    print("volviendo al menu anterior")
                    break
                else:
                    print("seleccione un numero valido")
        elif(option1 == 2):#listo
                print("historial\n")
                for history in range(len(log)):
                    print(log[history])
                while(True):
                    print("presione cualquier tecla para volver")
                    x = input()
                    break
        elif(option1 == 3):#listo
            q = PlayerMenu(7)
            print(NAMES)
            if(ListPlayer[0] == NAMES):
                print(q.secondMiniMenu(SuperHand,NAMES,personalCoin))
                print(q.secondMiniMenu(unknow[1],ListPlayer[1],CoinList[1]))
                print(q.secondMiniMenu(unknow[2],ListPlayer[2],CoinList[2]))
                if(n == 4):
                    print(q.secondMiniMenu(unknow[3],ListPlayer[3],CoinList[3]))
                print("cantidad de cartas en el mazo ",len(deck_list))
                while(True):
                    print("presione cualquier tecla para volver")
                    x = input()
                    break
        elif(option1 == 4):
            descripcion = PlayerMenu(6).menusplayers()
            print(descripcion)
            while(True):
                print("0 para volver")
                x == (input())
                break         
        else:
            print("ingrese un numero valido")



def main():
    #pruebas
    print("Welcome to COUP!")
    print("\n")
    Players_num = int(input("how many players are going to play?  "))
    while(True):
        if (Players_num < 3 or Players_num > 4):
            Players_num = int(input("They are a maximum of 4 and a minimum of 3: "))
        else:
            break
    print(Game(Players_num))
if __name__ == '__main__':
    main()