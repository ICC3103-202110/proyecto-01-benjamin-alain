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
        x = 1
        while(x < n):
            print(x,ListPlayer[x])
            x += 1
        print(n,"nadie quiere contraatacar")
        count = int(input("que jugador desea contratacar? "))
        if(count >= n):
            count = n
        if(count == n+1):
            return ListPlayer,n,count
        return ListPlayer,n,count
    def action(self):
        return "taxes"
