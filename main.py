from Winner import Won
from player import gambler
from assasin import murder
from Duke import Tax
from Menu import PlayerMenu
from random import shuffle
from Captain import Steal
playerlist = []
deck = []
def CreatePlayer(n):
    x = 1
    while (x<=n):
        name = input("your name: ")
        coin = 2
        card = int(input("your cards: "))
        playerlist.append(gambler(name,coin,card))
        x += 1
    return playerlist

def Deck():
    y = 1
    while(y<=3):
        deck.append(Tax("Duke"))
        deck.append(murder("asesino"))
        deck.append(Steal("capitan"))
        y += 1
    shuffle(deck)
    return deck

def main():
    #pruebas
    x = Deck()
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