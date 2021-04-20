class CardLost:
    def __init__(self, name):
        self.__name=name
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    
    def DropCard(L,U1,player_point,PD):               #para el jugador actual
        if player_point[0] == 2:                             #le queda una vida  Jugador turno actual
            count=0
            for i in L:
                print(count,i)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[0][0] == '??'):
                    U1[0].insert(0,L[0])
                    U1[0].remove('??')

            if(CardShow == 1):
                if(U1[0][0] == '??'):
                    U1[0].insert(1,L[CardShow])
                    U1[0].remove('??')

            player_point[0] -=1


        if player_point[0] == 1:              #Pierde la ultima vida Jugadr turno actual
            U1.pop(0)
            U1.insert(0,L)
            player_point[0] -= 1


        return U1
    def DropCard_2_n_3(L,U1,player_point,PD,n):       #para el jugador no actual n=3
        if player_point[1] ==  1:              #Jugador 2 pierde una vida.
            count=0
            for y in PD[1]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[1][0] == '??'):
                    U1[1].insert(0,PD[1][0])
                    U1[1].remove('??')

            if(CardShow == 1):
                if(U1[1][0] == '??'):
                    U1[1].insert(1,PD[1][1])
                    U1[1].remove('??')

        if player_point[1] == 0:                  #jugador 2 pierde su ultima vida.
            U1.pop(1)
            U1.insert(1,PD[1])


        if player_point[2] ==  1:              #Jugador 3 pierde una vida.
            count=0
            for y in PD[2]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[2][0] == '??'):
                    U1[2].insert(0,PD[2][0])
                    U1[2].remove('??')

            if(CardShow == 1):
                if(U1[2][0] == '??'):
                    U1[2].insert(1,PD[2][1])
                    U1[2].remove('??')



        if player_point[2] == 0:                  #jugador 3 pierde su ultima vida.
            U1.pop(2)
            U1.insert(2,PD[2])
        return U1
    
    def DropCard_2_n_4(L,U1,player_point,PD,n):       #Para el jugador no actual n=4
        if player_point[1] ==  1:              #Jugador 2 pierde una vida.
            count=0
            for y in PD[1]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[1][0] == '??'):
                    U1[1].insert(0,PD[1][0])
                    U1[1].remove('??')

            if(CardShow == 1):
                if(U1[1][0] == '??'):
                    U1[1].insert(1,PD[1][1])
                    U1[1].remove('??')
                    
        if player_point[1] == 0:                  #jugador 2 pierde su ultima vida.             
            U1.pop(1)
            U1.insert(1,PD[1])
        

        if player_point[2] ==  1:              #Jugador 3 pierde una vida.
            count=0
            for y in PD[2]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[2][0] == '??'):
                    U1[2].insert(0,PD[2][0])
                    U1[2].remove('??')

            if(CardShow == 1):
                if(U1[2][0] == '??'):
                    U1[2].insert(1,PD[2][1])
                    U1[2].remove('??')



        if player_point[2] == 0:                  #jugador 3 pierde su ultima vida.             
            U1.pop(2)
            U1.insert(2,PD[2])


        
        if player_point[3] ==  1:              #Jugador 4 pierde una vida.
            count=0
            for y in PD[3]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[3][0] == '??'):
                    U1[3].insert(0,PD[3][0])
                    U1[3].remove('??')

            if(CardShow == 1):
                if(U1[3][0] == '??'):
                    U1[3].insert(1,PD[3][1])
                    U1[3].remove('??')
            
        if player_point[3] == 0:
            if player_point[3] == 0:                  #jugador 4 pierde su ultima vida.             
                U1.pop(3)
                U1.insert(3,PD[3])
            
        
        return U1
    def DropCard_2_n_2(L,U1,player_point,PD,n):       #para el jugador no actual n=2
        if player_point[1] ==  1:                     #Jugador no actual pierde una vida.
            count=0
            for y in PD[1]:
                print(count,y)
                count+=1
            CardShow = int(input("elija entre las 2 cartas para botar: "))
            if(CardShow == 0):
                if(U1[1][0] == '??'):
                    U1[1].insert(0,PD[1][0])
                    U1[1].remove('??')

            if(CardShow == 1):
                if(U1[1][0] == '??'):
                    U1[1].insert(1,PD[1][1])
                    U1[1].remove('??')

        if player_point[1] == 0:                       #jugador no actual pierde su ultima vida.
            U1.pop(1)
            U1.insert(1,PD[1])


        return U1