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
    objeto=Deck_cards("Name_card_object")
    x = objeto.first_round(l)
    for i in range(len(x)):
        print(x[i].name)
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
    List = CreatePlayer(3)
    print(x.efect(List))
    q = PlayerMenu(4)
    print(q.playersMiniMenu("nada",List[0]))
    #luego se selecciona a quien quitarle la influencia carta

if __name__ == '__main__':
    main()