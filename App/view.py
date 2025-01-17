﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
from os import get_terminal_size
import config as cf
import time
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

  
terminalSize = get_terminal_size()[0]

def initDatabase():
  return controller.init()


def loadData(database):
  files = {
    '1': 'UFOS-utf8-small.csv',
    '2': 'UFOS-utf8-5pct.csv',
    '3': 'UFOS-utf8-10pct.csv',
    '4': 'UFOS-utf8-20pct.csv',
    '5': 'UFOS-utf8-30pct.csv',
    '6': 'UFOS-utf8-50pct.csv',
    '7': 'UFOS-utf8-80pct.csv',
    '8': 'UFOS-utf8-large.csv',
  }

  print('Seleccione el archivo que desea cargar: ')
  print('1. UFOS-utf8-small')
  print('2. UFOS-utf8-5pct')
  print('3. UFOS-utf8-10pct')
  print('4. UFOS-utf8-20pct')
  print('5. UFOS-utf8-30pct')
  print('6. UFOS-utf8-50pct')
  print('7. UFOS-utf8-80pct')
  print('8. UFOS-utf8-large')

  file = files.get(input('> '), None)

  if file is None:
    loadData(database)
  else:
    controller.loadData(database, file)
    print('\n' + ('-' * terminalSize))
    string = 'Se cargaron ' + str(lt.size(database['sightings'])) + ' avistamientos.'
    print('\n', ' ' * ((terminalSize // 2) - len(string) // 2 - 1), string, ' ' * ((terminalSize - (terminalSize // 2)) - len(string) - 1))
    print('\n' + ('-' * terminalSize))

    print('\n\nLos primeros 5 avistamientos cargados son:\n')
    for i in lt.iterator(lt.subList(database['sightings'], 1, 5)):
      print('\n' + ('-' * terminalSize) + '\n')
      printSighting(i)

    print('\n' + ('-' * terminalSize) + '\n\n\n')

    print('\n\nLos ultimos 5 avistamientos cargados son:\n')
      
    for i in lt.iterator(lt.subList(database['sightings'], (lt.size(database['sightings']) - 5), 5)):
      print('\n' + ('-' * terminalSize) + '\n')
      printSighting(i)

    print('\n' + ('-' * terminalSize) + '\n\n')


#=============================
#           REQ. 1
#=============================

def getOrderedCitiesByCount(database, city):

  info = controller.getOrderedCitiesByCount(database, city)

  string = 'Contar los avistamientos en una ciudad'
  print('\n' + '=' * ((terminalSize // 2) - len(string) // 2), string, '=' * ((terminalSize // 2) - len(string) // 2 - 1))

  print('\nHay', lt.size(info[0]), 'diferentes ciudades con avistamientos de OVNIs...')
  print('El Top 5 de las ciudades con más avistamientos de OVNIs es:')

  for j in lt.iterator(lt.subList(info[0], 1, 5)):
    i = lt.firstElement(j)
    print('\n' + ('-' * terminalSize) + '\n')
    print('Ciudad:', i['city'] + ', Cantidad:', lt.size(j))
  
  print('\n' + ('-' * terminalSize) + '\n')

  print('Hay', lt.size(info[1]), 'avistamientos en la ciudad de:', city)
  print('\n\nLos primeros 3 avistamientos en la ciudad son:\n')

  for i in lt.iterator(lt.subList(info[1], 1, 3)):
    print('\n' + ('-' * terminalSize) + '\n')
    printSighting(i)
  
  print('\n' + ('-' * terminalSize) + '\n')
  
  print('\n\nLos ultimos 3 avistamientos en la ciudad son:\n')

  for i in lt.iterator(lt.subList(info[1], lt.size(info[1]) - 3, 3)):
    print('\n' + ('-' * terminalSize) + '\n')
    printSighting(i)
  
  
  print('\n' + ('-' * terminalSize) + '\n')


#=============================
#           REQ. 2
#=============================

def getOrderedSightingsByDuration(database, minTime, maxTime):

  info = controller.getOrderedSightingsByDuration(database, minTime, maxTime)

  string = 'Contar los avistamientos por duración'
  print('\n' + '=' * ((terminalSize // 2) - len(string) // 2), string, '=' * ((terminalSize // 2) - len(string) // 2 - 1))

  print('\nHay', lt.size(info[0]), 'diferentes duraiones por avistamiento de OVNIs...')
  print('El Top 5 de las duraciones de avistamientos de OVNIs más largas es:')

  for j in lt.iterator(lt.subList(info[0], 1, 5)):
    i = lt.firstElement(j)
    print('\n' + ('-' * terminalSize) + '\n')
    print('Duración:', i['duration (seconds)'] + ', Cantidad:', lt.size(j))
  
  print('\n' + ('-' * terminalSize) + '\n')

  print('Hay', lt.size(info[1]), 'avistamientos entre:', minTime, 'and', maxTime, 'duration.')
  print('\n\nLos primeros 3 avistamientos con la duración especificada son:\n')

  for i in lt.iterator(lt.subList(info[1], 1, 3)):
    print('\n' + ('-' * terminalSize) + '\n')
    printSighting(i)
  
  print('\n' + ('-' * terminalSize) + '\n')
  
  print('\n\nLos ultimos 3 avistamientos con la duración especificada son:\n')

  for i in lt.iterator(lt.subList(info[1], lt.size(info[1]) - 3, 3)):
    print('\n' + ('-' * terminalSize) + '\n')
    printSighting(i)
  
  print('\n' + ('-' * terminalSize) + '\n')

#=============================
#           REQ. 3
#=============================

def getSightsByHour(database, timeMinor, timeMaximun):
  data = controller.getSightsByHour(database, timeMinor, timeMaximun)

  print("There are "+ str(lt.size(data[0])) + " UFO sightings with different times [hh:mm:ss]...")
  print("The last UFO sighting is: \n")

  last = lt.subList(data[0], lt.size(data[0]), 1)

  for i in lt.iterator(last):
    print("> "+str(i["hourIndex"])+" : "+ str(lt.size(i["sightings"]))+ "\n")

  print("There are "+str(lt.size(data[1]))+" sightings between"+timeMinor+ " and "+ timeMaximun)

  first3 = lt.subList(data[1], 1, 3)
  last3 = lt.subList(data[1], lt.size(data[1]) - 2, 3)

  print("The first 3 and last 3 UFO sightings in this time are: ")
  for sight in lt.iterator(first3):
    print('\nFecha y hora:', sight['datetime'])
    print('Ciudad:', sight['city'])
    print('Estado:', sight['state'])
    print('País:', sight['country'])
    print('Duración(s):', sight['duration (seconds)'])
    print('Forma:', sight['shape'])
    print("------------------------------------------------\n")
        
  for sight in lt.iterator(last3):
    print('\nFecha y hora:', sight['datetime'])
    print('Ciudad:', sight['city'])
    print('Estado:', sight['state'])
    print('País:', sight['country'])
    print('Duración(s):', sight['duration (seconds)'])
    print('Forma:', sight['shape'])
    print("------------------------------------------------\n")


#=============================
#           REQ. 4
#=============================

def getSightsBetweenDates(database, startDate, endDate):
  data = controller.getSightsBetweenDates(database, startDate, endDate)

  print('Hay', lt.size(data[0]), 'diferentes fechas.')
  print('El top 5 más antiguo es: \n')
  
  top5 = lt.subList(data[0], 1, 5)
    
  sorted = controller.sortByDate(top5)

  for duration in lt.iterator(sorted):
    print(duration['date'], ':', lt.size(duration['sightings']))
    
  print('\nThere are', lt.size(data[1]), 'UFO sightings between the dates.')
  print('First 3 and last 3 sightings are: ')

  for sighting in lt.iterator(lt.subList(data[1], 1, 3)):
    print('\nFecha y hora:', sighting['datetime'])
    print('Ciudad:', sighting['city'])
    print('Estado:', sighting['state'])
    print('País:', sighting['country'])
    print('Duración(s):', sighting['duration (seconds)'])
    print('Forma:', sighting['shape'])
    print("\n------------------------------------------------\n")
        
  for sighting in lt.iterator(lt.subList(data[1], lt.size(data[1]) - 2, 3)):
    print('\nFecha y hora:', sighting['datetime'])
    print('Ciudad:', sighting['city'])
    print('Estado:', sighting['state'])
    print('País:', sighting['country'])
    print('Duración(s):', sighting['duration (seconds)'])
    print('Forma:', sighting['shape'])
    print("\n------------------------------------------------\n")
    

#=============================
#           REQ. 5
#=============================

def getOrderedSightingsByLocation(database, minLatitude, maxLatitude, minLongitude, maxLongitude):
  print(controller.getOrderedSightingsByLocation(database, minLatitude, minLongitude, maxLatitude, maxLongitude))


def testTime(function, *args):
  initialTime = time.time_ns()
  function(*args)
  finalTime = (time.time_ns() - initialTime) / 1000000000
  print('El proceso fue completado de forma exitosa en:', str(round(finalTime, 3)) + 's')


def printSighting(sighting):
  print('Fecha y hora: ', sighting['datetime'])
  print('Ciudad: ', sighting['city'])
  print('Estado: ', sighting['state'])
  print('País: ', sighting['country'])
  print('Forma: ', sighting['shape'])
  print('Duración(s): ', sighting['duration (seconds)'])
  print('Duración(h/m): ', sighting['duration (hours/min)'])
  print('Comentarios:')
  print('\t*', sighting['comments'].replace('&#44', ','))
  print('Fecha de publicación', sighting['date posted'])
  print('Coordenadas:')
  print('\tLatitud:', sighting['latitude'])
  print('\tLongitud:', sighting['longitude'])


def printTestTimeMenu():
  print("Prueba de tiempo de ejecución")
  print("1- Cargar información en la base de datos")
  print("2- Contar los avistamientos en una ciudad")
  print("3- Contar los avistamientos por duración")
  print("6- Contar los avistamientos de una Zona Geográfica")


def printMenu():
  print("Bienvenido")
  print("1- Cargar información en la base de datos")
  print("2- Contar los avistamientos en una ciudad")
  print("3- Contar los avistamientos por duración")
  print("4- Contar avistamientos por Hora/Minutos del día")
  print("5- Contar los avistamientos en un rango de fechas")
  print("6- Contar los avistamientos de una Zona Geográfica")
  print("7- Prueba de tiempo de ejecución")

database = None

"""
Menu principal
"""
while True:
  printMenu()
  inputs = input('Seleccione una opción para continuar\n> ')
  if int(inputs[0]) == 1:
    print("Cargando información de los archivos ....")
    database = initDatabase()
    loadData(database)
  elif int(inputs[0]) == 2:
    city = input('Ingresa la ciudad: \n> ')
    getOrderedCitiesByCount(database, city)
  elif int(inputs[0]) == 3:
    minTime = input('Ingresa la cantidad minima de segundos: \n> ')
    maxTime = input('Ingresa la cantidad maxima de segundos: \n> ')
    getOrderedSightingsByDuration(database, minTime, maxTime)
  elif int(inputs[0]) == 4:
    time1 = input("Ingrese la hora en la que inicia el intervalo (HH:MM) \n> ")
    time2 = input("Ingrese la hora en la que finaliza el intervalo (HH:MM) \n> ")
    getSightsByHour(database, time1, time2)
  elif int(inputs[0]) == 5:
    startDate = input("Ingrese la fecha inicial del intervalo (AAAA-MM-DD) \n> ")
    endDate = input("Ingrese la fecha final del intervalo (AAAA-MM-DD) \n> ")
    getSightsBetweenDates(database, startDate, endDate)
  elif int(inputs[0]) == 6:
    minLatitude = input('Ingresa la latitud minima: ')
    maxLatitude = input('Ingresa la latitud maxima: ')
    minLongitude = input('Ingresa la longitud minima: ')
    maxLongitude = input('Ingresa la longitud maxima: ')
    getOrderedSightingsByLocation(database, minLatitude, maxLatitude, minLongitude, maxLongitude)
  elif int(inputs[0]) == 7:
    printTestTimeMenu()
    functionToTest = int(input('Seleccione la función a probar:\n> ')[0])
    if functionToTest == 1:
      database = initDatabase()
      testTime(controller.loadData, database, 'UFOS-utf8-large.csv')
    if functionToTest == 2:
      testTime(controller.getOrderedCitiesByCount, database, 'las vegas')
  else:
    sys.exit(0)
sys.exit(0)
