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
PrincipalDeck = []

def CreatePlayer1(n):
    x = 1
    while (x<=n):
        name = input("your name: ")
        coin = 2
        card = 2
        playerlist.append(gambler(name,coin,card))
        x += 1
    return playerlist

def main():
    #pruebas

    l=[]
    deck_list=[]
    objeto=Deck_cards("Name_card_object")
    x = objeto.first_round(l)
    handplayer1 = objeto.hand(player1,x)
    handplayer2 = objeto.hand(player2, handplayer1[1])
    handplayer3 = objeto.hand(player3, handplayer2[1])
    handplayer4 = objeto.hand(player4, handplayer3[1])
    for i in range(len(handplayer4[0])):
        JAND1.append(handplayer1[0][i].name)
        JAND2.append(handplayer2[0][i].name)
        JAND3.append(handplayer2[0][i].name)
        JAND4.append(handplayer4[0][i].name)
    for i in range(len(handplayer4[1])):
        deck_list.append(handplayer4[1][i].name)
    print(deck_list)
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
    List = CreatePlayer1(3)
    print(x.efect(List))
    q = PlayerMenu(4)
    print(q.playersMiniMenu(JAND1,List[0]))
    #luego se selecciona a quien quitarle la influencia carta


print("Welcome to COUP!")
print("\n")
Players_num = int(input("how many players are going to play?  "))
if Players_num == 3:
    print("wichipirichi")
    if __name__ == '__main__':
        main()