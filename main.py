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
            deck_list.append(handplayer3[1][i].name)
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
                    personalCoin += 7
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
                    break
                elif(option2 == 1):
                    print("se a seleccionado la ayuda extranjera")
                    personalCoin += 2 #agregar contrataque (duke)
                    ingresolog = [NAMES+" obtiene 2 moneda por ayuda extranjera"]
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
                elif(option2 == 2 or personalCoin >= 10):
                    print("se a seleccionado el golpe\n")
                    x = 0
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
                    break
                elif(option2 == 5):
                    print("se a seleccionado la Extorsión")
                elif(option2 == 6):
                    print("se a seleccionado el Cambio")
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
                print(q.secondMiniMenu(incognita,ListPlayer[1],CoinList[1]))
                print(q.secondMiniMenu(incognita,ListPlayer[2],CoinList[2]))
                if(n == 4):
                    print(q.secondMiniMenu(incognita,ListPlayer[3],CoinList[3]))
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
