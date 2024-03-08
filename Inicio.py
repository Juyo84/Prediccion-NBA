import DatosEquipo as Datos

"""

    RECORD CASA Y VISITA
    RATING OFENSIVO Y DEFENSIVO
    PUNTOS A FAVOR, EN CONTRA Y DIFERENCIAL
    RESULTADOS ULT. 5 ENCUENTROS
    RESULTADOS DE ANTERIORES ENCUENTROS CON EL RIVAL
    RESULTADOS ULT. 5 ENCUENTROS DEPENDIENDO C/V

"""

def getDatosEquipos(equipoCasa, equipoVisita):

    datosEquipoCasa = Datos.setDatosEquipo(equipoCasa, equipoVisita, 'Casa')
    datosEquipoVisita = Datos.setDatosEquipo(equipoVisita, equipoCasa, 'Visitante')

    print(datosEquipoCasa)
    print(datosEquipoVisita)
    
    return datosEquipoCasa, datosEquipoVisita

#==========================================================#

def calculoEncuentros(resultadoEquipo):

    victorias = 0
    derrotas = 0
    
    rachaVictoria = 0
    rachaDerrota = 0
    rachaActual = 0
    
    rachaV = 0
    rachaD = 0

    for encuentro in reversed(resultadoEquipo):

        if encuentro == 'W':

            victorias += 1
            
            rachaD = 0
            rachaV += 1

            if rachaV > rachaVictoria:

                rachaVictoria = rachaV

            if rachaActual >= 0:

                rachaActual += 1

            else:

                rachaActual = 1

        else:

            derrotas += 1
            
            rachaV = 0
            rachaD += 1

            if rachaD > rachaDerrota:

                rachaDerrota = rachaD            

            if rachaActual <= 0:

                rachaActual -= 1

            else:

                rachaActual = -1

    porcentajeVictorias = (victorias * 100) / (victorias + derrotas)

    return porcentajeVictorias, rachaActual, rachaVictoria, rachaDerrota

#==========================================================#

def calculoPorcentajeVictoria(recordEquipo):
    
    victorias = ''

    for num in recordEquipo:

        if num.isdigit():

            victorias = victorias + num

        elif num == '-':

            derrotas = recordEquipo[len(victorias) + 1:]
            break

    porcentajeVictoria = (int(victorias) * 100) / (int(victorias) + int(derrotas))

    return porcentajeVictoria

#==========================================================#

def diferencialEstadistica(estadisticaCasa, estadisticaVisita):

    casaOfensiva = float(estadisticaCasa[0])
    casaDefensiva = float(estadisticaCasa[1])
    
    visitaOfensiva = float(estadisticaVisita[0])
    visitaDefensiva = float(estadisticaVisita[1])
    
    promedioCasa = (casaOfensiva + casaDefensiva) / 2
    promedioVisita = (visitaOfensiva + visitaDefensiva) / 2
    
    casa = 0
    visita = 0

    if casaOfensiva > visitaDefensiva:

        casa += 1

    elif casaOfensiva < visitaDefensiva:

        visita += 1

    
    if casaDefensiva > visitaOfensiva:
    
       casa += 1

    elif casaDefensiva < visitaOfensiva:

        visita += 1


    if casaOfensiva > visitaOfensiva:

        casa += 1

    elif casaOfensiva < visitaOfensiva:

        visita += 1


    if casaDefensiva > visitaDefensiva:

        casa += 1

    elif casaDefensiva < visitaDefensiva:

        visita += 1
    
    
    if promedioCasa > promedioVisita:

        casa += 1

    elif promedioCasa < promedioVisita:

        visita += 1
    

    if casa > visita:

        return 'Casa'
    
    elif casa < visita:

        return 'Visitante'
    
#==========================================================#

datosEquipos = getDatosEquipos('Los Angeles Clippers', 'Los Angeles Lakers')

#print(calculoPorcentajeVictoria(datosEquipos[0][0][0][0]))
#print(calculoPorcentajeVictoria(datosEquipos[0][0][0][1]))
#print(diferencialEstadistica(datosEquipos[0][0][1], datosEquipos[1][0][1]))
#print(diferencialEstadistica(datosEquipos[0][0][2], datosEquipos[1][0][2]))
#print(calculoEncuentros(datosEquipos[1][0][3]))
#print(calculoEncuentros(datosEquipos[1][0][4]))
#print(calculoEncuentros(datosEquipos[1][0][5]))