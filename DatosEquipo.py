from bs4 import BeautifulSoup
import requests

def getPuntos(equipo, response):
    
    if equipo == 'Los Angeles Clippers':

        ciudad = 'L.A. Clippers'
    
    elif equipo == 'Los Angeles Lakers':

        ciudad = 'L.A. Lakers'

    elif equipo == 'Golden State Warriors':
    
        ciudad = 'Golden St.'

    elif equipo == 'Portland Trail Blazers':
    
        ciudad = 'Portland'
        
    elif len(equipo.split()) > 2:

        ciudad = equipo.split()[0] + ' ' + equipo.split()[1]

    else:

        ciudad = equipo.split()[0]

    soup = BeautifulSoup(response.text, 'html.parser')
        
    tablaEsteRecord = soup.find_all('table')[0].find('tbody')
    tablaOesteRecord = soup.find_all('table')[1].find('tbody')
        
    #REGISTRA EL RECORD DE CASA, DE VISITA Y DIFERENCIAL
    for filaEste in tablaEsteRecord.find_all('tr'):

        if filaEste.find_all('td')[1].find('a') != None:
                
            if ciudad in filaEste.find_all('td')[1].text:
                
                recordCasa = filaEste.find_all('td')[6].text.strip()
                recordVisitante = filaEste.find_all('td')[7].text.strip()

                dataRecord = recordCasa, recordVisitante
                return dataRecord

    for filaOeste in tablaOesteRecord.find_all('tr'):

        if filaOeste.find_all('td')[1].find('a') != None:
                
            if ciudad in filaOeste.find_all('td')[1].text:
            
                recordCasa = filaOeste.find_all('td')[6].text.strip()
                recordVisitante = filaOeste.find_all('td')[7].text.strip()
                recordDiferencial = filaOeste.find_all('td')[8].text.strip()

                dataRecord = recordCasa, recordVisitante, recordDiferencial
                return dataRecord

#==========================================================#

def getRecord(equipo, response):

    if equipo == 'Los Angeles Clippers':

        ciudad = 'L.A. Clippers'
    
    elif equipo == 'Los Angeles Lakers':

        ciudad = 'L.A. Lakers'

    else:

        ciudad = equipo.split()[0]

    soup = BeautifulSoup(response.text, 'html.parser')
        
    tablaEsteRecord = soup.find_all('table')[0].find('tbody')
    tablaOesteRecord = soup.find_all('table')[1].find('tbody')
        
    #REGISTRA EL RECORD DE CASA Y DE VISITA
    for filaEste in tablaEsteRecord.find_all('tr'):

        if filaEste.find_all('td')[1].find('a') != None:
                
            if ciudad in filaEste.find_all('td')[1].text:
                
                recordCasa = filaEste.find_all('td')[9].text.strip()
                recordVisitante = filaEste.find_all('td')[10].text.strip()

                dataRecord = recordCasa, recordVisitante
                return dataRecord

    for filaOeste in tablaOesteRecord.find_all('tr'):

        if filaOeste.find_all('td')[1].find('a') != None:
                
            if ciudad in filaOeste.find_all('td')[1].text:
                
                recordCasa = filaOeste.find_all('td')[9].text.strip()
                recordVisitante = filaOeste.find_all('td')[10].text.strip()

                dataRecord = recordCasa, recordVisitante
                return dataRecord

#==========================================================#

def getRating(equipo, response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaRating = soup.find('table').find('tbody')

    #REGISTRA EL RATING OFENSIVO Y DEFENSIVO
    for fila in tablaRating.find_all('tr'):
            
        if fila.find_all('td')[0] != None:

            if equipo == fila.find_all('td')[0].find('a').text:
                
                ratingOfensivo = fila.find_all('td')[7].text
                ratingDefensivo = fila.find_all('td')[8].text

    dataRating = ratingOfensivo, ratingDefensivo

    return dataRating

#==========================================================#

def getEncuentrosGeneral(response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaEncuentros = soup.find('table').find('tbody')
    numEncuentro = 0
    resultadoEncuentro = []

    #REGISTRA LOS RESULTADOS DE LOS ULT. 5 ENCUENTROS
    for fila in reversed(tablaEncuentros.find_all('tr')):
            
        if fila.find('th').text != 'Rk' and fila.find('th').text != '':
                
            resultadoEncuentro.append(fila.find_all('td')[4].text)
            numEncuentro = numEncuentro + 1

        if numEncuentro >= 5:

            return resultadoEncuentro

#==========================================================#
    
def getEncuentrosRival(equipoRival, response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaEncuentros = soup.find('table').find('tbody')
    dataEncuentrosRival = []

    #REGISTRA LOS RESULTADOS DE LOS ULT. 5 ENCUENTROS CONTRA EL RIVAL
    for fila in tablaEncuentros.find_all('tr'):

        if fila.find('th').text != 'Rk' and fila.find('th').text != '':
                
            if  equipoRival == fila.find_all('td')[3].find('a').text:
                    
                dataEncuentrosRival.append(fila.find_all('td')[4].text)
        
    return dataEncuentrosRival

#==========================================================#

def getEncuentrosCV(response, lugar):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaEncuentros = soup.find('table').find('tbody')
    resultadoEncuentros = []
    numeroEncuentros = 0

    #REGISTRA LOS RESULTADOS DE LOS ULT. 5 ENCUENTROS SEGUN C/V
    for fila in reversed(tablaEncuentros.find_all('tr')):
            
        if fila.find('th').text != 'Rk' and fila.find('th').text != '':
                
            if fila.find_all('td')[2].text == lugar:

                resultadoEncuentros.append(fila.find_all('td')[4].text)
                numeroEncuentros = numeroEncuentros + 1

            if numeroEncuentros >= 5:

                return resultadoEncuentros
                    
    return resultadoEncuentros

#==========================================================#

def getfechaEncuentros(response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaDescansos = soup.find('table').find('tbody')
    numEncuentro = 0
    fechaPartido = []

    #REGISTRA FECHA DE LOS ULT. 5 ENCUENTROS
    for fila in reversed(tablaDescansos.find_all('tr')):
            
        if fila.find('th').text != 'Rk' and fila.find('th').text != '':
                
            fechaPartido.append(fila.find_all('td')[1].text)
            numEncuentro = numEncuentro + 1

        if numEncuentro >= 5:
            
            return fechaPartido

#==========================================================#

def getSimpleRating(equipo, response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaSimpleRatingEste = soup.find_all('table')[0].find('tbody')
    tablaSimpleRatingOeste = soup.find_all('table')[1].find('tbody')

    #REGISTRA EL SIMPLE RATING SYSTEM
    for filaEste in tablaSimpleRatingEste.find_all('tr'):

        if filaEste.find_all('td')[0] != None:

            if equipo == filaEste.find('th').find('a').text:
                                
                simpleRating = filaEste.find_all('td')[6].text

                return (simpleRating)


    for filaOeste in tablaSimpleRatingOeste.find_all('tr'):
            
        if filaOeste.find_all('td')[0] != None:

            if equipo == filaOeste.find('th').find('a').text:
                
                simpleRating = filaOeste.find_all('td')[6].text

                return (simpleRating)

#==========================================================#

def getMargenVictoria(equipo, response):

    soup = BeautifulSoup(response.text, 'html.parser')

    tablaRating = soup.find('table').find('tbody')

    #REGISTRA EL MARGEN DE VICTORIA Y NET RATING
    for fila in tablaRating.find_all('tr'):
            
        if fila.find_all('td')[0] != None:

            if equipo == fila.find_all('td')[0].find('a').text:
                
                margenVictoria = fila.find_all('td')[6].text
                netRating = fila.find_all('td')[9].text

    dataMargen = margenVictoria, netRating

    return dataMargen

#==========================================================#

def getClasificacionCBS():

    url = 'https://www.cbssports.com/nba/standings/'
    responseCBS = requests.get(url)

    return responseCBS

#==========================================================#

def getClasificacionBR():

    url = 'https://www.basketball-reference.com/leagues/NBA_2024_standings.html'
    responseBR = requests.get(url)

    return responseBR

#==========================================================#

def getRatings():

    url = 'https://www.basketball-reference.com/leagues/NBA_2024_ratings.html'
    responseRatings = requests.get(url)

    return responseRatings

#==========================================================#

def getPartidosEquipo(siglas):

    url = 'https://www.basketball-reference.com/teams/' + siglas +  '/2024/gamelog/'
    responsePTO = requests.get(url)

    return responsePTO

#==========================================================#

def setDatosEquipo(equipo, rival, lugar):

    datosEquipo = []

    if equipo == 'Los Angeles Lakers':

        siglasEquipo = 'LAL'

    elif equipo == 'Los Angeles Clippers':

        siglasEquipo = 'LAC'

    elif equipo == 'New York Knicks':

        siglasEquipo = 'NYK'

    elif equipo == 'Brooklyn Nets':

        siglasEquipo = 'BRK'
        
    elif equipo == 'Charlotte Hornets':

        siglasEquipo = 'CHO'
        
    elif equipo == 'Golden State Warriors':

        siglasEquipo = 'GSW'

    elif equipo == 'San Antonio Spurs':

        siglasEquipo = 'SAS'

    elif equipo == 'Oklahoma City Thunder':

        siglasEquipo = 'OKC'

    elif equipo == 'New Orleans Pelicans':

        siglasEquipo = 'NOP'

    else:
        
        siglasEquipo = equipo[0:3].upper()


    if rival == 'Los Angeles Lakers':

        siglasRival = 'LAL'

    elif rival == 'Los Angeles Clippers':

        siglasRival = 'LAC'

    elif rival == 'New York Knicks':

        siglasRival = 'NYK'

    elif rival == 'Brooklyn Nets':

        siglasRival = 'BRK'
        
    elif rival == 'Charlotte Hornets':

        siglasRival = 'CHO'
        
    elif rival == 'Golden State Warriors':

        siglasRival = 'GSW'

    elif rival == 'San Antonio Spurs':

        siglasRival = 'SAS'

    elif rival == 'Oklahoma City Thunder':

        siglasRival = 'OKC'

    elif rival == 'New Orleans Pelicans':

        siglasRival = 'NOP'

    else:

        siglasRival = rival[0:3].upper()


    if lugar == 'Visitante':

        busqueda = '@'

    else:

        busqueda = ''
    
    responseClasificacionCBS = getClasificacionCBS()
    responseClasificacionBR = getClasificacionBR()
    responsePartidos = getPartidosEquipo(siglasEquipo)
    responseRatings = getRatings()

    if responseRatings.status_code == 200 and responseClasificacionCBS.status_code == 200 and responseClasificacionBR.status_code == 200 and responsePartidos.status_code == 200:

        """
            0. RECORD CASA Y VISITA
            1. RATING OFENSIVO Y DEFENSIVO
            2. PUNTOS A FAVOR, EN CONTRA Y DIFERENCIAL
            3. RESULTADOS ULT. 5 ENCUENTROS
            4. RESULTADOS DE ANTERIORES ENCUENTROS CON EL RIVAL
            5. RESULTADOS ULT. 5 ENCUENTROS DEPENDIENDO C/V
            6. FECHA ULT. 5 ENCUENTROS
            7. SIMPLE RATING SYSTEM
            8. MARGEN DE VICTORIA Y NET RATING
        """

        datosEquipo.append([
            getRecord(equipo, responseClasificacionCBS),
            getRating(equipo, responseRatings),
            getPuntos(equipo, responseClasificacionCBS),
            getEncuentrosGeneral(responsePartidos),
            getEncuentrosRival(siglasRival, responsePartidos),
            getEncuentrosCV(responsePartidos, busqueda),
            getfechaEncuentros(responsePartidos),
            getSimpleRating(equipo, responseClasificacionBR),
            getMargenVictoria(equipo, responseRatings)
                            ])

        return datosEquipo
    
    else:
        
        return setDatosEquipo(equipo, rival, lugar)





""" SIN DECIDIR
def getJugadores(equipo):

    if equipo == 'Los Angeles Lakers':

        siglas = 'LAL'

    elif equipo == 'Los Angeles Clippers':

        siglas = 'LAC'

    else:
        
        siglas = equipo[0:3].upper()
    
    url = 'https://www.basketball-reference.com/teams/' + siglas + '/2024.html'
    response = requests.get(url)
    
    dataJugadoresEquipo = []

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        tablaEquipo = soup.find_all('table')[0]

        #REGISTRA LOS JUGADORES DEL EQUIPO
        for fila in tablaEquipo.find_all('tr'):

            if fila.find('td') != None:

                jugador = fila.find('td').find('a').text
                urlJugador = fila.find('td').find('a', {'href': True})['href']
                historialJugador = getDatosJugador(urlJugador)

                dataJugadoresEquipo.append([jugador, urlJugador, historialJugador])

        return dataJugadoresEquipo
    
    else:

        print("ERROR AL LEER LA PAGINA DE PTS EQUIPO")
        return getJugadores(equipo)

#==========================================================#

#ESTA OCUPA LA FUNCION getJugadores
def getDatosJugador(jugador):

    dataJugador = []

    url = 'https://www.basketball-reference.com' + jugador
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        tablaUlt5Pts = soup.find_all('table')[0]

        #REGISTRA LOS PTS DE LOS ULTIMOS 5 PARTIDOS
        for fila in tablaUlt5Pts.find_all('tr'):

            if fila.find_all('td') != []:

                puntos = fila.find_all('td')

                dataJugador.append(puntos[23].text)

        return dataJugador
    
    else:

        print("ERROR AL LEER LA PAGINA DEL JUGADOR")
        return getDatosJugador(jugador)
"""