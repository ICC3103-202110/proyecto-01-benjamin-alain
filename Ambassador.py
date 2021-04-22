from IEespecial import IEspecialAtack
from random import shuffle,random

class Exchange(IEspecialAtack):

    def __init__(self,name):
        super().__init__(name)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "AMBASSADOR"
        else:
            self.__name = "AMBASSADOR"
 
    
    def efect(self,Deck,Card):       #card es una lista de las carats que tiene el jugador #Descke s el mazo
        l=[]
        if len(Card) == 1:       
            l.append(Card[0])
            l.append(Deck[0])
            l.append(Deck[1])
            for i in range (len(l)):
                print(i,l[i])  
            t=int(input("Elige el numero de la carta que quieras tomar: "))  
            if t == 0:
                Card[0]=l[0]
            elif t == 1:
                Card[0]=l[1]
            elif t == 2:
                Card[0]=l[2]      
            else:
                print("Esto no esta permito")
                for i in range (len(l)):
                    print(i,l[i])  
                t=int(input("Elige el numero de la carta que quieras tomar: "))  
                
            shuffle(Deck)
        

        if len(Card) == 2:       
            l.append(Card[0])
            l.append(Card[1])
            l.append(Deck[0])
            l.append(Deck[1])
            for i in range (len(l)):
                print(i,l[i])  
            t=int(input("Elige el numero de la primera carta que quieras tomar: "))  

            if t == 0:
                Card[0]=l[0]
                l.remove(Card[t])
            elif t == 1:
                Card[0]=l[1]
                l.remove(Card[t])
            elif t == 2:
                Card[0]=l[2]
                l.remove(Deck[t-2])
            elif t == 3:
                Card[0]=l[3]
                l.remove(Deck[t-2])
            else:
                print("Esto no esta permito,Intentelo denuevo")
                print("\n")
                for i in range (len(l)):
                    print(i,l[i])  
                t=int(input("Elige el numero de la primera carta que quieras tomar: ")) 
    
    
            for u in range(len(l)):
                print(u,l[u])       
            r=int(input("Elige el numero de la segunda carta que quieras tomar: "))

            if r == 0:
                Card[1]=l[0]
                
            elif r == 1:
                Card[1]=l[1]
                
            elif r == 2:
                Card[1]=l[2]
        

            else:
                print("Esto no esta permito,Intentelo denuevo")
                print("\n")
                print(u)
                for u in range(len(l)):
                    print(u,l[u])        
                r=int(input("Elige el numero de la segunda carta que quieras tomar: "))
        
            
            shuffle(Deck)   
                 
        print("Tus nuevas cartas son: ", Card)
        return Card
    
    def counter(self, extorsion):
        if(extorsion == True):
            extorsion = False
        print("se bloquea la extorsion")
        return extorsion

    def action(self):
        return "Exchange"
    
    #def MenuOption(self)