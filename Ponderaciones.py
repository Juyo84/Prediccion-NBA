import DatosEquipo as Datos
from datetime import datetime

def getDatosEquipos(equipoCasa, equipoVisita):

    datosEquipoCasa = Datos.setDatosEquipo(equipoCasa, equipoVisita, 'Casa')
    datosEquipoVisita = Datos.setDatosEquipo(equipoVisita, equipoCasa, 'Visitante')
    
    return datosEquipoCasa, datosEquipoVisita

#==========================================================#

def calculoEncuentros(resultadoEquipo):

    victorias = 0
    derrotas = 0

    porcentajeVictorias = 0

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


    if victorias + derrotas > 0:
    
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

def calculoDescansos(fechasEquipo):

    descansos = []

    for i in range(4):

        fechaActual = datetime.strptime(fechasEquipo[i], "%Y-%m-%d")
        fechaSiguiente = datetime.strptime(fechasEquipo[i + 1], "%Y-%m-%d")
        descansos.append((fechaActual - fechaSiguiente).days)

    return descansos

#==========================================================#

def diferencialEstadistica(estadisticaCasa, estadisticaVisita):
    
    if len(estadisticaCasa) <= 0 or len(estadisticaVisita) <= 0:

        return (0, 0)

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

        casa += 2
    
    elif casa < visita:

        visita += 2

    return (casa, visita)
    
#==========================================================#

def diferencialVictoria(victoriasCasa, victoriasVisita):

    if victoriasCasa > victoriasVisita:

        return (1, 0)

    elif victoriasCasa < victoriasVisita:

        return (0, 1)
    
    else:

        return (1, 1)

#==========================================================#

def diferencialEncuentros(encuentrosCasa, encuentrosVisita):

    porcentajeCasa = encuentrosCasa[0]
    rachaActualCasa = encuentrosCasa[1]
    rachaVictoriaCasa = encuentrosCasa[2]
    rachaDerrotaCasa = encuentrosCasa[3]

    porcentajeVisita = encuentrosVisita[0]
    rachaActualVisita = encuentrosVisita[1]
    rachaVictoriaVisita = encuentrosVisita[2]
    rachaDerrotaVisita = encuentrosVisita[3]

    casa = 0
    visita = 0

    if porcentajeCasa > porcentajeVisita:

        casa += 1

    elif porcentajeCasa < porcentajeVisita:

        visita += 1


    if rachaActualCasa > 0:

        casa += 1

    else:

        casa -= 1    
    
    if rachaActualVisita > 0:

        visita += 1

    else:

        visita -= 1


    if rachaActualCasa > rachaActualVisita:

        casa += 2

    elif rachaActualCasa < rachaActualVisita:

        visita += 2
    
    if rachaVictoriaCasa > rachaVictoriaVisita:

        casa += 1

    elif rachaVictoriaCasa < rachaVictoriaVisita:

        visita += 1


    if rachaDerrotaCasa > rachaDerrotaVisita:

        casa += 1

    elif rachaDerrotaCasa < rachaDerrotaVisita:

        visita += 1

    
    if casa > visita:

        casa += 2
    
    elif casa < visita:

        visita += 2

    return (casa, visita)

#==========================================================#

def diferencialDescansos(descansosCasa, descansosVisita):

    for i in range(len(descansosCasa)):

        if descansosCasa[i] > descansosVisita[i]:

            return (2, 0)
        
        elif descansosCasa[i] < descansosVisita[i]:

            return (0, 2)
    
    return (0, 0)

#==========================================================#

def diferencialSimpleRating(SRCasa, SRVisita):

    if SRCasa > SRVisita:

        return (1, 0)
    
    elif SRCasa < SRVisita:

        return (0, 1)
    
    else:
        
        return (0, 0)

#==========================================================#

def ganadorV1(casa, visita):

    datosEquipos = getDatosEquipos(casa, visita)
    
    porcentajeCasa = calculoPorcentajeVictoria(datosEquipos[0][0][0][0])
    porcentajeVisita = calculoPorcentajeVictoria(datosEquipos[1][0][0][1])

    encuentrosGeneralCasa = calculoEncuentros(datosEquipos[0][0][3])
    encuentrosGeneralVisita = calculoEncuentros(datosEquipos[1][0][3])

    encuentrosRivalCasa = calculoEncuentros(datosEquipos[0][0][4])
    encuentrosRivalVisita = calculoEncuentros(datosEquipos[1][0][4])

    encuentrosCVCasa = calculoEncuentros(datosEquipos[0][0][5])
    encuentrosCVVisita = calculoEncuentros(datosEquipos[1][0][5])
    
    ganadorVictoria = diferencialVictoria(porcentajeCasa, porcentajeVisita)

    ganadorRating = diferencialEstadistica(datosEquipos[0][0][1], datosEquipos[1][0][1])
    ganadorPuntos = diferencialEstadistica(datosEquipos[0][0][2], datosEquipos[1][0][2])

    ganadorEncuentrosGeneral = diferencialEncuentros(encuentrosGeneralCasa, encuentrosGeneralVisita)
    ganadorEncuentrosRival = diferencialEncuentros(encuentrosRivalCasa, encuentrosRivalVisita)
    ganadorEncuentrosCV = diferencialEncuentros(encuentrosCVCasa, encuentrosCVVisita)
    
    ganadores = ganadorVictoria, ganadorRating, ganadorPuntos, ganadorEncuentrosGeneral, ganadorEncuentrosRival, ganadorEncuentrosCV

    ponderacionCasa = 0
    ponderacionVisita = 0
    
    for ganador in ganadores:

        ponderacionCasa += ganador[0]
        ponderacionVisita += ganador[1]

    if ponderacionCasa > ponderacionVisita:

        return casa
    
    elif ponderacionCasa < ponderacionVisita:

        return visita
    
    else:

        return 'Empate'

def ganadorV2(casa, visita):

    datosEquipos = getDatosEquipos(casa, visita)
    
    porcentajeCasa = calculoPorcentajeVictoria(datosEquipos[0][0][0][0])
    porcentajeVisita = calculoPorcentajeVictoria(datosEquipos[1][0][0][1])

    encuentrosGeneralCasa = calculoEncuentros(datosEquipos[0][0][3])
    encuentrosGeneralVisita = calculoEncuentros(datosEquipos[1][0][3])

    encuentrosRivalCasa = calculoEncuentros(datosEquipos[0][0][4])
    encuentrosRivalVisita = calculoEncuentros(datosEquipos[1][0][4])

    encuentrosCVCasa = calculoEncuentros(datosEquipos[0][0][5])
    encuentrosCVVisita = calculoEncuentros(datosEquipos[1][0][5])

    descansosCasa = calculoDescansos(datosEquipos[0][0][6])
    descansosVisita = calculoDescansos(datosEquipos[1][0][6])
    
    ganadorVictoria = diferencialVictoria(porcentajeCasa, porcentajeVisita)

    ganadorRating = diferencialEstadistica(datosEquipos[0][0][1], datosEquipos[1][0][1])
    ganadorPuntos = diferencialEstadistica(datosEquipos[0][0][2], datosEquipos[1][0][2])

    ganadorEncuentrosGeneral = diferencialEncuentros(encuentrosGeneralCasa, encuentrosGeneralVisita)
    ganadorEncuentrosRival = diferencialEncuentros(encuentrosRivalCasa, encuentrosRivalVisita)
    ganadorEncuentrosCV = diferencialEncuentros(encuentrosCVCasa, encuentrosCVVisita)

    ganadorDescanso = diferencialDescansos(descansosCasa, descansosVisita)

    ganadorSimpleRating = diferencialSimpleRating(datosEquipos[0][0][7], datosEquipos[1][0][7])
    
    ganadores = ganadorVictoria, ganadorRating, ganadorPuntos, ganadorEncuentrosGeneral, ganadorEncuentrosRival, ganadorEncuentrosCV, ganadorDescanso, ganadorSimpleRating

    ponderacionCasa = 0
    ponderacionVisita = 0
    
    for ganador in ganadores:

        ponderacionCasa += ganador[0]
        ponderacionVisita += ganador[1]

    if ponderacionCasa > ponderacionVisita:

        return casa
    
    elif ponderacionCasa < ponderacionVisita:

        return visita
    
    else:

        return 'Empate'

#==========================================================#
