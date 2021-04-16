from tabulate import tabulate

class PlayerMenu:
    def __init__(self,options):
        self.__options = options
    
    @property
    def options(self):
        return self.__options
    @options.setter
    def options(self, value):
        if value <0:
            self.__options = 1
        else:
            self.__options = value
    
    def menusplayers(self):
        if (self.options == 1):
            Headers = ["numero","accion"]
            principal = [["1.","ejecutar una accion"], 
                        ["2.","ver el log"],
                        ["3.","ver cartas"],
                        ["4.", "descripcion de las cartas"]]
            print(tabulate(principal,headers=Headers,tablefmt='grid'))
            x = int(input("seleccione el numero: "))
            return x
        elif (self.options == 2):
            Headers = ["numero", "Acciones"]
            playermenu = [["ingreso"],["ayuda externa"],["golpe"],
                            ["Impuestos (duke)"],["Asesinato (asesino)"],
                            ["Extorsión (Capitán)"],["Cambio (Embajador)"],
                            ["volver"]]
            print(tabulate(playermenu,headers=Headers,showindex=True,tablefmt='grid'))
            y = int(input("seleccione el numero: "))
            return y
        elif(self.options == 3):
            print("contrataques")
            Headers = ["numero", "CONTRATAQUES"]
            countermenu = [["Bloquear ayuda extranjera (Duque)"],
                            ["Bloquear asesinato (Condesa)"],
                            ["Bloquear extorsión (Embajador/Capitán)"]]

            print((tabulate(countermenu,headers=Headers,showindex=True,tablefmt='grid')))
            z = int(input("seleccione el numero del contraataque: "))
            return z
        elif(self.options == 5):
            HEADERS = ["numero", "opcion"]
            counteroptions = [["desafio"],["CONTRATAQUES"]]
            print((tabulate(counteroptions,headers=HEADERS,showindex=True,tablefmt='grid')))   
            r =  int(input("seleccione el numero de las opciones: "))
            return ""        
        
        elif(self.options == 6):
            descp= [["Caracter","Action","Effect","Counteraction"],
                    ["No special card needed", "Income", "Take 1 coin","NONE"],
                    ["No special card needed","Forein Aid", "Take 2 coin","NONE"],
                    ["No special card needed","Coup","Pay 7 coins","NONE"],
                    ["Duke","Tax","Take 3 coins","Blocks Foreign Aid"],
                    ["Assassin","Assassinate","Pay 3 coins","NONE"],
                    ["Ambassador","Exchange","Exchange cards with Court Deck","Blocks stealling"],
                    ["Captain","Steal","Take 2 coins from another player","Blocks stealling"],
                    ["Contessa","NONE","NONE","Blocks assassination"]
                    ]

            print(tabulate(descp, headers='firstrow'))
            return ""

        
    def playersMiniMenu(self, deck, player):
        if (self.options == 4):
            HEADERS = ["",player.name]
            #ejemplo
            lista = deck
            minimenu = [["coins",player.coins],["cards",lista]]
            print(tabulate(minimenu,headers=HEADERS,tablefmt='grid'))
            return ""
    def secondMiniMenu(self,deck,player,coin):
        if(self.options == 7):
            HEADERS = ["",player]
            #ejemplo
            lista = deck
            minimenu = [["coins",coin],["cards",lista]]
            print(tabulate(minimenu,headers=HEADERS,tablefmt='grid'))
            return ""
    def objetive(self,n,OtherList,Otherdeck):
        if(self.options == 8):
            x = 0
            L = []
            while(x<n):
                fila = [x,OtherList[x],Otherdeck[x]]
                L.append(fila)
                x += 1
            L.pop(0)
            for i in range(len(L)):
                print(L[i])
            return ""
    def MiniMenu(self,gloval):
        if(self.options == 9):
            print(tabulate(gloval,tablefmt='grid'))
            return ""