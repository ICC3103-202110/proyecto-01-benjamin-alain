from Duke import Tax
from Assassin import murder
from Captain import Steal
from Contessa import Block
from Ambassador import Exchange
import random

class Deck_cards:

    def __init__(self,name):
        self.__name = name

    def first_round(self, starting_deck):
        
        y = 1
        while(y<=3):
            starting_deck.append(Tax("Duke"))
            starting_deck.append(murder("Asesino"))
            starting_deck.append(Steal("capitan"))
            starting_deck.append(Block("Contessa"))
            starting_deck.append(Exchange("Ambassador"))
            y += 1
        shuffle(starting_deck)
        return starting_deck