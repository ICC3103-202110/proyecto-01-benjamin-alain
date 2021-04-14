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

def Game(n):
    l=[]
    deck_list=[]
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
    print(deck_list)
    print(JAND1)
    print(JAND2)
    print(JAND3)
    if(n == 4):
        print(JAND4)
    y = PlayerMenu(1)
    z = PlayerMenu(2)
    w = PlayerMenu(5)
    print(y.menusplayers())
    print(z.menusplayers())
    if (w.menusplayers() == 0):
        print("hola")
    x = murder("")
    coin = 6
    coin = (x.MoneyLess(coin))
    print(coin)
    ALLDeck.append(JAND1)
    ALLDeck.append(JAND2)
    ALLDeck.append(JAND3)
    List = CreatePlayer1(3,ALLDeck)

    print(x.efect(List))
    q = PlayerMenu(4)
    print(q.playersMiniMenu(JAND1,List[0]))
    print(q.playersMiniMenu(JAND2,List[1]))
    print(q.playersMiniMenu(JAND3,List[2]))
    #print(q.playersMiniMenu(JAND1,List[3]))
    #luego se selecciona a quien quitarle la influencia carta

def MoneyLess(coin,n):
    print("pay 3 coins and eliminate a influence (show card): ")
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
