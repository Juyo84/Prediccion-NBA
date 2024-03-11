import Ponderaciones as Ganador
import Resultados
from os import system

def nombreEquipo(equipo):

    equiposNBA = ["Toronto Raptors", "Brooklyn Nets", "New York Knicks", "Boston Celtics", "Philadelphia 76ers",
     "Indiana Pacers", "Chicago Bulls" ,"Cleveland Cavaliers", "Detroit Pistons", "Milwaukee Bucks",
     "Miami Heat", "Washington Wizards", "Charlotte Bobcats", "Atlanta Hawks", "Orlando Magic",
     "Los Angeles Clippers", "Golden State Warriors", "Phoenix Suns", "Sacramento Kings", "Los Angeles Lakers",
     "San Antonio Spurs", "Houston Rockets", "Memphis Grizzlies", "Dallas Mavericks", "New Orleans Pelicans",
     "Oklahoma City Thunder", "Portland Trail Blazers", "Minnesota Timberwolves", "Denver Nuggets", "Utah Jazz"]

    for equipoNBA in equiposNBA:

        if equipo.lower() in equipoNBA.lower():

            return equipoNBA
        
    return "NINGUNO"
        
#==========================================================#

def menu():

    system("cls")
    
    res = 0

    while res != 1 and res != 2 and res != 3:

        print("==========   PREDICCIONES NBA   ==========\n\n" +
            "1. Prediccion\n" +
            "2. Resultados\n" +
            "3. Cerrar\n")
    
        res = input()
        
        system("cls")

        if res.isnumeric():

            res = int(res)

            if res != 1 and res != 2 and res != 3:

                print("INTRODUZCA VALORES DEL 1 AL 3\n")

        else:

            print("INTRODUZCA VALORES DEL 1 AL 3\n")
        
    if res == 1:

        equipoCasa = "NINGUNO"
        equipoVisita = "NINGUNO"

        while equipoCasa == "NINGUNO":
            
            system("cls")
            print("Equipo Casa:")

            equipoCasa = input()
            equipoCasa = nombreEquipo(equipoCasa)
        
        while equipoVisita == "NINGUNO":

            system("cls")
            print("Equipo Visita:")

            equipoVisita = input()
            equipoVisita = nombreEquipo(equipoVisita)
        
        system("cls")
        print("==========   CALCULANDO   ==========")

        equipoGanadorV1 = Ganador.ganadorV1(equipoCasa, equipoVisita)
        equipoGanadorV2 = Ganador.ganadorV2(equipoCasa, equipoVisita)

        system("cls")
        print("==========   EQUIPO GANADOR   ==========\n\n" +
              "Version 1: " + equipoGanadorV1 + "\n" +
              "Version 2: " + equipoGanadorV2 + "\n")

        input()

    elif res == 2:

        system("cls")
        print("APARTADO DE RESULTADOS")
        input()

    elif res == 3:

        system("cls")
        print("Cerrando Programa")

        return
    
    return menu()

#==========================================================#

menu()