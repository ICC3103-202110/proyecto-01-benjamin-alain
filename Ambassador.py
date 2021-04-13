from IEespecial import IEspecialAtack

class Tax(IEspecialAtack):

    def __init__(self,name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if value == "":
            self.__name = "AMBASSADOR"
        else:
            self.__name = value
    

    
    
    
    
    def efect(self,Deck,Card):       #card es una lista de las carats que tiene el jugador #Descke s el mazo
    l=[]
    if len(Card) == 1:       
        l.append(Card[0])
        l.append(Deck[0])
        l.append(Deck[1])
        for i in range (len(l)):
            print(i,l[i])  
        t=int(input("Choose the number of the card yo wanna pick: "))  

        if t == 0:
            Card[0]=l[0]
        elif t == 1:
            Card[0]=l[1]
        elif t == 2:
            Card[0]=l[2]      
        else:
            print("This number is not allowed")
            for i in range (len(l)):
                print(i,l[i])  
            t=int(input("Choose the number of the card yo wanna pick: "))  


    if len(Card) == 2:       
        l.append(Card[0])
        l.append(Card[1])
        l.append(Deck[0])
        l.append(Deck[1])
        for i in range (len(l)):
            print(i,l[i])  
        t=int(input("Choose the number of the first card yo wanna pick: "))  

        if t == 0:
            Card[0]=l[0]
            l.remove(Card[0])
        elif t == 1:
            Card[0]=l[1]
            l.remove(Card[1])
        elif t == 2:
            Card[0]=l[2]
            l.remove(Deck[0])
        elif t == 3:
            Card[0]=l[3]
            l.remove(Deck[1])
        else:
            print("This number is not allowed, TRY AGAIN")
            print("\n")
            for i in range (len(l)):
                print(i,l[i])  
            t=int(input("Choose the number of the first card yo wanna pick: ")) 
        
        
        for u in range(len(l)):
            print(u,l[u])       
        r=int(input("Choose the number of the second card yo wanna pick: "))

        if r == 0:
            Card[1]=l[0]
            l.remove(Card[0])
        elif r == 1:
            Card[1]=l[1]
            l.remove(Card[1])
        elif r == 2:
            Card[1]=l[2]
            l.remove(Deck[0])

        else:
            print("This number is not allowed, TRY AGAIN")
            print("\n")
            print(u)
            for u in range(len(l)):
                print(u,l[u])        
            r=int(input("Choose the number of the second card yo wanna pick: "))
    
    
    
    
    
    
    
    
    def counter(self,Steal):
        #el counter es bloquear robar del capitan
        if(Steal == True):
            Steal = False
        print("se bloquea el capitan")
        return Steal
    
    
    
    
    
    
    
    def action(self):
        return "taxes"
