

class Won:

    def __init__(self, player1,player2,player3,player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
    
    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self,value):
        if value < 0:
            self.__player1 = 0
        else:
            self.__player1 = value
    
    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self,value):
        if value < 0:
            self.__player2 = 0
        else:
            self.__player2 = value

    @property
    def player3(self):
        return self.__player3
    @player3.setter
    def player3(self,value):
        if value < 0:
            self.__player3 = 0
        else:
            self.__player3 = value

    @property
    def player4(self):
        return self.__player4
    @player4.setter
    def player4(self,value):
        if value < 0:
            self.__player4 = 0
        else:
            self.__player4 = value
    
    def Wons(self, TotalPlayer):
            if(TotalPlayer == 4):
                if(self.player1 > self.player2 and
                self.player1 > self.player3 and 
                self.player1 > self.player4):
                    return "Ganador jugador 1"
                elif(self.player2 > self.player1 and
                self.player2 > self.player3 and 
                self.player2 > self.player4):
                    return "Ganador jugador 2"
                elif(self.player3 > self.player1 and
                self.player3 > self.player2 and 
                self.player3 > self.player4):
                    return "Ganador jugador 3"
                elif(self.player4 > self.player1 and
                self.player4 > self.player3 and 
                self.player4 > self.player2):
                    return "Ganador jugador 4"
            elif(TotalPlayer == 3):
                if(self.player1 > self.player2 and 
                self.player1 > self.player3):
                    return "Ganador jugador 1"
                elif(self.player2 > self.player1 and 
                self.player2 > self.player3):
                    return "Ganador jugador 2"
                elif(self.player3 > self.player2 and 
                self.player3 > self.player1):
                    return "Ganador jugador 1"