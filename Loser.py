class CardLost:
    def __init__(self, name):
        self.__name=name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    
    def DropCard(self,SuperHand,PersonalDeck,ListPlayer,unknow):
        count = 0
        for i in range(len(SuperHand)):
            print(i,SuperHand[i])
        CardShow = int(input("elija entre las 2 cartas para botar: "))
        if(CardShow == 0):
            if(unknow[0][0] == '??'):
                unknow[0].insert(0,SuperHand[CardShow])
                unknow[0].remove('??')
                return unknow
        if(CardShow == 1):
            if(unknow[0][0] == '??'):
                unknow[0].insert(1,SuperHand[CardShow])
                unknow[0].remove('??')
                return unknow
                '''
                if(unknow[0][0] != '??'):
                    count += 1
                if (count == 1):
                    print("perdiste ;(")
                '''
