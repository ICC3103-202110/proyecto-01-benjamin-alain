from IEespecial import IEspecialAtack

class Tax(IEspecialAtack):

    def __init__(self,name):
        super().__init__(name)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "DUKE"
        else:
            self.__name = "DUKE"
    
    def efect(self,coins):
        x = coins + 3
        return x
    
    def counter(self,ListPlayer,n):
        print("QUIEN QUIERE CONTRAATACAR?: ")
        print(1,ListPlayer[1])
        print(2,ListPlayer[2])
        if(n == 4):
            print(3,ListPlayer[3])
            print(4,"nadie quiere contraatacar ")
            print("\n")
            count = int(input("que jugador desea contratacar? "))
            if(count == 4):
                return ListPlayer,n,count
            return ListPlayer,n,count
        else:
            print(3,"nadie quiere contraatacar ")
            print("\n")
            count = int(input("que jugador desea contratacar? "))
            if(count == 3):
                return ListPlayer,n,count
            return ListPlayer,n,count                

    def action(self):
        return "taxes"
