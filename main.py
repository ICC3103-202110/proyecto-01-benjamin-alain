from Winner import Won
from player import gambler
from assasin import murder
from Duke import Tax
playerlist = []

def CreatePlayer(n):
    x = 1
    while (x<n):
        name = input("your name: ")
        coin = 2
        card = int(input("your cards: "))
        playerlist.append(gambler(name,coin,card))
        x += 1
    return playerlist

def main():
    x = murder("")
    coin = 6
    coin = (x.MoneyLess(coin))
    print(coin)
    List = CreatePlayer(3)
    print(x.efect(List))
    #luego se selecciona a quien quitarle la influencia carta

if __name__ == '__main__':
    main()