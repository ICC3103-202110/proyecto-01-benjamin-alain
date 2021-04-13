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
            playermenu = [["ingreseo"],["ayuda externa"],["golpe"],
                            ["Impuestos (duke)"],["Asesinato (asesino)"],
                            ["Extorsión (Capitán)"],["Cambio (Embajador)"]]
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
        
    def playersMiniMenu(self, deck, player):
        if (self.options == 4):
            HEADERS = ["",player.name]
            lista = ["duque","capitan"]
            minimenu = [["coins",player.coins],["cards",lista]]
            print(tabulate(minimenu,headers=HEADERS,tablefmt='grid'))