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
from THEGAME import Ex
from Loser import CardLost


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
        name = input("your name: ")
        coin = 2
        card = hand[x-1]
        point = 2
        playerlist.append(gambler(name,coin,card,point))
        x += 1
    return playerlist


def Game(n):
    l = []
    pointplayer = []
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
        pointplayer.append(List[i].points)
    unknow = []
    unknow.append(incognita)
    unknow.append(incognita)
    unknow.append(incognita) 
    if(n == 4):
        unknow.append(incognita)   
    LOG = []
    log = []
    GlobalList3 = []
    GlobalList4 = []
    turns = 0
    GlobalTurns = 0
    GlobalList3.append(ListPlayer)
    GlobalList3.append(PersonalDeck)
    GlobalList3.append(CoinList)
    TheGame = Ex("princiPAL").PrincipalGame(GlobalList3,ListPlayer,PersonalDeck,CoinList,log,unknow,n,deck_list,pointplayer)
    print(TheGame)


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