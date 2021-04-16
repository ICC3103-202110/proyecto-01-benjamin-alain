class Ex:

    def __init__(self,algo):
        self.__algo = algo
    
    @property
    def algo(self):
        return self.__algo
    @algo.setter
    def algo(self,value):
        self.__algo = value
    
    def Sort_Board(self,turns,n,gloval):
        
        if turns == 0:    #jugador 1
            if n==3:
                gloval[1].pop(1)
                gloval[1].pop(1)
                gloval[1].insert(1,["??","??"])
                gloval[1].insert(1,["??","??"])
                return gloval

            if n==4:
                gloval[1].pop(1)
                gloval[1].pop(1)
                gloval[1].pop(1)
                gloval[1].insert(1,["??","??"])
                gloval[1].insert(1,["??","??"])
                gloval[1].insert(1,["??","??"])
                return gloval

        if turns == 1:         #jugador 2
            if n == 3:
                gloval[1].pop(0)
                gloval[1].pop(1)
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(2,["??","??"])
                return gloval

            if n==4:
                gloval[1].pop(0)
                gloval[1].pop(1)
                gloval[1].pop(1)
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(2,["??","??"])
                gloval[1].insert(2,["??","??"])
                return gloval

        if turns == 2:         #jugador 3
            if n == 3:
                gloval[1].pop(0)
                gloval[1].pop(0)
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(0,["??","??"])
                return gloval

            if n==4:
                gloval[1].pop(0)
                gloval[1].pop(0)
                gloval[1].pop(1)
                gloval[1].insert(1,["??","??"])
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(0,["??","??"])
                return gloval

        if turns == 3:         #jugador 4
            if n==4:
                gloval[1].pop(0)
                gloval[1].pop(0)
                gloval[1].pop(0)
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(0,["??","??"])
                gloval[1].insert(0,["??","??"])
                return gloval
