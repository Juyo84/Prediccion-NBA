import pandas as pd
import os

def partidoPrediccion(fecha, casa, visita, ganadorV1, ganadorV2, ganadorV3):

    datosPartido = []
    datosPartido.append([fecha, casa, visita, ganadorV1, ganadorV2, ganadorV3, 'Desconocido'])
    
    dfNuevo = pd.DataFrame(datosPartido, columns=('Fecha', 'Casa', 'Visitante', 'Ganador V1', 'Ganador V2', 'Ganador V3', 'Ganador Final'))

    if os.path.isfile('Archivos//Resultados.csv'):

        dfExistente = pd.read_csv('Archivos//Resultados.csv')
        datosActualizados = pd.concat([dfExistente, dfNuevo], ignore_index=True)
        datosActualizados.to_csv('Archivos//Resultados.csv', index=False)
    
    else:

        dfNuevo.to_csv('Archivos//Resultados.csv', index=False)
    
    return 'Guardado exitosamente'

#==========================================================#

def partidoGanador(fecha, casa, visita, ganador):

    dfExistente = pd.read_csv("Archivos//Resultados.csv")
    
    dfExistente.loc[(dfExistente['Fecha'] == fecha) & (dfExistente['Casa'] == casa) & (dfExistente['Visitante'] == visita), 'Ganador Final'] = ganador
    
    dfActualizado = pd.DataFrame(dfExistente, columns=('Fecha', 'Casa', 'Visitante', 'Ganador V1', 'Ganador V2', 'Ganador V3', 'Ganador Final'))
    dfActualizado.to_csv('Archivos//Resultados.csv', index=False)

    return 'Guardado exitosamente'

