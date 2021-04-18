from Duke import Tax
from Assasin import murder
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
from random import shuffle

class Deck_cards:

    def __init__(self,name):
        self.__name = name

    def first_round(self, starting_deck):
        
        y = 1
        while(y<=3):
            starting_deck.append(Tax("Duke"))
            starting_deck.append(murder("Asesino"))
            starting_deck.append(Steal("Capitan"))
            starting_deck.append(Block("Contessa"))
            starting_deck.append(Exchange("Ambassador"))
            y += 1
        shuffle(starting_deck)
        return starting_deck
    
    def hand(self,playerdeck,General):
        playerdeck.append(General[0])
        playerdeck.append(General[1])
        General.pop(0)
        General.pop(0)
        shuffle(General)
        shuffle(playerdeck)
        return playerdeck, General