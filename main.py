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

def CreatePlayer1(n, hand):
    x = 1
    while (x<=n):
        print("\n")
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
    ALLDeck.append(incognita)
    List = CreatePlayer1(n,ALLDeck)  
    PersonalDeck = ALLDeck
    if (n == 3):
        PersonalDeck.pop(3)
    if(n == 4):
        PersonalDeck.pop(4)
    for i in range(len(List)):
        ListPlayer.append(List[i].name)
        CoinList.append(List[i].coins)
    unknow = []
    print(PersonalDeck)
    for i in range(len(PersonalDeck)):
        unknow.append(incognita)
    print(unknow)
    LOG = []
    log = []
    while(True):
        NAMES = ListPlayer[0]
        SuperHand = PersonalDeck[0]
        personalCoin = CoinList[0]
        print("le toca a:  ", NAMES)
        part1 = PlayerMenu(1)
        obj = PlayerMenu(8)
        option1 = part1.menusplayers()
        if(option1 == 1):
            part2 = PlayerMenu(2)
            option2 = part2.menusplayers()
            while(True):
                if(option2 == 0):
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
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    print()
                    break
                elif(option2 == 1):
                    print("se a seleccionado la ayuda extranjera")
                    ingresolog = [NAMES+" obtiene 2 moneda por ayuda extranjera"]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    personalCoin += 2 #agregar contrataque (duke)
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
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
                    personalCoin -= 7
                    obj.objetive(n,ListPlayer,PersonalDeck)
                    print("")
                    elecction = int(input("escoja la victima del golpe: "))
                    ingresolog = [NAMES+", a golpeado a, "+ListPlayer[elecction]]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    break
                elif(option2 == 3):
                    print("se a seleccionado el Impuestos")
                    duke = Tax("Duke")
                    DUKE = duke.efect(personalCoin)
                    personalCoin = DUKE
                    ingresolog = [NAMES +" utiliza la accion "+ duke.action() +" ganado 3 monedas"]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    break
                elif(option2 == 4):
                    print("se a seleccionado el Asesinato")
                    personalCoin -= 3 
                    print(personalCoin)
                    Assassin = murder("Asesino")
                    ASSASIN = Assassin.efect(ListPlayer,CoinList,unknow,n)  
                    elecction = int(input("escoja la victima del asesinato: "))
                    print(elecction)    
                    MurderVictim = ListPlayer[elecction]
                    print(MurderVictim)
                    print("solo puede mirar "+MurderVictim)
                    for i in range(len(PersonalDeck[elecction])):
                        print(i,PersonalDeck[elecction][i])
                    victimelection = int(input("jugador, "+MurderVictim+ " elija su carta "))     
                    Over = (PersonalDeck[elecction][victimelection])
                    print(Over)
                    print(remplazo(Over))
                    unknow.pop(elecction)
                    print(unknow)
                    unknow.insert(elecction,(remplazo(Over)))
                    print(unknow)
                    PersonalDeck.pop(elecction)
                    #PersonalDeck.insert(elecction,remplazo(Over))
                    ingresolog = [NAMES+ ", utiliza la accion "+Assassin.action()+" contra "+MurderVictim]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    break
                elif(option2 == 5):

                    print("se a seleccionado la Extorsión")
                    Captain = Steal("Capitan")
                    extor = True
                    CAPTAIN = Captain.efect(ListPlayer,1,CoinList,n)
                    print(CAPTAIN)
                    elecction = int(input("escoja la victima del robo: "))
                    victimPlayer = ListPlayer[elecction]
                    victimCoinss = CoinList[elecction]
                    if (victimCoinss < 2):
                        victimCoins = CoinList[elecction]-1
                    elif(victimCoinss == 0):
                        print("no puede robar a esta persona")
                    else:
                        victimCoins = CoinList[elecction]-2
                    CoinList.insert(elecction,victimCoins)
                    ingresolog = [NAMES+", utiliza la accion "+Captain.action()+" para robar monedas a, "+victimPlayer]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    personalCoin += 2 
                    print(personalCoin)
                    CoinList.append(personalCoin)
                    CoinList.pop(0)
                    print(CoinList)
                    CoinList.pop(n-1)
                    print(CoinList)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    shuffle(deck_list)
                    break
                    
                elif(option2 == 6):
                    print("se a seleccionado el Cambio")
                    Ambassador = Exchange("Emabajador")
                    AMBASSADOR = Ambassador.efect(deck_list,SuperHand)
                    ingresolog = [NAMES + " utiliza la accion "+Ambassador.action()+" cambiando cartas"]
                    log.append(ingresolog)
                    ListPlayer.pop(0)
                    ListPlayer.append(NAMES)
                    PersonalDeck.pop(0)
                    PersonalDeck.append(SuperHand)
                    CoinList.pop(0)
                    CoinList.append(personalCoin)
                    NAMES = ListPlayer[0]
                    SuperHand = PersonalDeck[0]
                    personalCoin = CoinList[0]
                    shuffle(deck_list)
                    shuffle(deck_list)
                    break
                elif(option2 == 7):
                    print("volviendo al menu anterior")
                    break
                else:
                    print("seleccione un numero valido")
        elif(option1 == 2):
                print("historial\n")
                for history in range(len(log)):
                    print(log[history])
                while(True):
                    print("presione cualquier tecla para volver")
                    x = input()
                    break
        elif(option1 == 3):
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


    '''
    print(q.playersMiniMenu(JAND3,List[2]))
    if(n == 4):
        print(q.playersMiniMenu(JAND4,List[3]))
    '''
    #luego se selecciona a quien quitarle la influencia carta




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
