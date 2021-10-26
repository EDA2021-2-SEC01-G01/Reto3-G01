"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as ms
from datetime import datetime as dt
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newDatabase():
  database = {}

  database['sightings'] = lt.newList('ARRAY_LIST')

  database['cityIndex'] = om.newMap(omaptype='RBT')

  database['dateIndex'] = om.newMap(omaptype='RBT')

  database['secondsIndex'] = om.newMap(omaptype='RBT', comparefunction=compareBySecondsAsc)

  database['locationsIndex'] = om.newMap(omaptype='RBT', comparefunction=compareCoors)

  return database


# Funciones para agregar informacion al catalogo

def addSighting(database, sighting):
  lt.addLast(database['sightings'], sighting)
  updateCityIndex(database['cityIndex'], sighting)
  updateDateIndex(database['dateIndex'], sighting)
  updateSecondsIndex(database['secondsIndex'], sighting)
  updateCoorsIndex(database['locationsIndex'], sighting)
  return database

def updateDateIndex(map, sighting):
  sightingTime = newTime(sighting['datetime'])
  entry = om.get(map, sightingTime.date())

  if entry is None:
    dateEntry = newDateEntry(sighting)
    om.put(map, sightingTime.date(), dateEntry)
  else:
    dateEntry = me.getValue(entry)


def updateCityIndex(map, sighting):
  sightingCityKey = newCityKey(sighting['city'])
  sightingTime = newTime(sighting['datetime'])
  entry = om.get(map, sightingCityKey)

  if entry is None:
    cityEntry = newCityEntry(sightingTime.date(), sighting)
    om.put(map, sightingCityKey, cityEntry)
  else:
    cityEntry = me.getValue(entry)
    om.put(cityEntry, sightingTime.date(), sighting)


def updateSecondsIndex(map, sighting):
  seconds = float(sighting['duration (seconds)'])
  cityCountryKey = sighting['city'] + sighting['country']

  entry = om.get(map, seconds)

  if entry is None:
    secondsEntry = newSecondsEntry(cityCountryKey, sighting)
    om.put(map, seconds, secondsEntry)
  else:
    secondsEntry = me.getValue(entry)
    om.put(secondsEntry, cityCountryKey, sighting)


def updateCoorsIndex(map, sighting):
  coors = sighting['latitude'] + '_' + sighting['longitude']
  datetimeKey = newTime(sighting['datetime']).date()

  entry = om.get(map, coors)

  if entry is None:
    coorsEntry = newCoorsEntry(datetimeKey, sighting)
    om.put(map, coors, coorsEntry)
  else:
    coorsEntry = me.getValue(entry)
    om.put(coorsEntry, datetimeKey, sighting)

# Funciones para creacion de datos

def newDateEntry(sighting):
  entry = lt.newList(datastructure='SINGLE_LINKED')
  lt.addLast(entry, sighting)

  return entry


def newCityEntry(sightingTime, sighting):
  entry = om.newMap(omaptype='RBT')
  om.put(entry, sightingTime, sighting)

  return entry


def newSecondsEntry(sightingCityCountry, sighting):
  entry = om.newMap(omaptype='RBT')
  om.put(entry, sightingCityCountry, sighting)

  return entry


def newCoorsEntry(sightingTime, sighting):
  entry = om.newMap(omaptype='RBT')
  om.put(entry, sightingTime, sighting)

  return entry


def newCityKey(city):
  key = ''

  for i in city:
    key += str(ord(i))

  return int(key)


def newTime(stringTime):
  return dt.strptime(stringTime, '%Y-%m-%d %H:%M:%S')

# Funciones de consulta

def getOrderedCitiesByCount(database, city):
  cityEntry = om.get(database['cityIndex'], city)

  cities = om.valueSet(database['cityIndex'])
  sightingsByCity = om.valueSet(me.getValue(cityEntry))

  ms.sort(cities, sortByCitySightings)

  listCities = lt.newList('SINGLE_LINKED')

  for i in lt.iterator(cities):
    lt.addLast(listCities, om.valueSet(i))

  return (listCities, sightingsByCity)


def getOrderedSightingsByDuration(database, minTime, maxTime):

  durationsEntry = om.values(database['secondsIndex'], minTime, maxTime)

  durations = om.valueSet(database['secondsIndex'])

  listDurations = lt.newList('SINGLE_LINKED')

  for i in lt.iterator(durations):
    lt.addLast(listDurations, om.valueSet(i))

  durationsEntryList = lt.newList('SINGLE_LINKED')

  for i in lt.iterator(durationsEntry):
    for j in lt.iterator(om.valueSet(i)):
      lt.addLast(durationsEntryList, j)

  ms.sort(durationsEntryList, sortByDatetime)

  return (listDurations, durationsEntryList)


def getOrderedSightingsByLocation(database, minLocation, maxLocation):

  locationsEntry = om.values(database['locationsIndex'], minLocation, maxLocation)

  listLocations = lt.newList('SINGLE_LINKED')

  for i in lt.iterator(locationsEntry):
    for j in lt.iterator(om.valueSet(i)):
      lt.addLast(listLocations, j)

  ms.sort(listLocations, sortByLocation)

  return listLocations


# Funciones de comparacion

def compareBySecondsAsc(key1, key2):
  if key1 == key2:
    return 0
  elif key1 < key2:
    return 1
  else:
    return -1


def isLongestLocation(key1, key2):
  latitude = key1.split('_')[0]
  longitude = key1.split('_')[1]

  latitude2 = key2.split('_')[0]
  longitude2 = key2.split('_')[1]

  if latitude > latitude2:
    return True
  elif longitude > longitude2:
    return True
  else:
    return False


def compareCoors(key1, key2):
  if key1 == key2:
    return 0
  elif not isLongestLocation(key1, key2):
    return -1
  else:
    return 1


# Funciones de ordenamiento

def sortByCitySightings(sighting1, sighting2):
  return om.size(sighting1) > om.size(sighting2)


def sortByDatetime(sighting1, sighting2):
  return newTime(sighting1['datetime']).date() < newTime(sighting2['datetime']).date()


def sortByLocation(sighting1, sighting2):
  coors1 = sighting1['latitude'] + '_' + sighting1['longitude']
  coors2 = sighting2['latitude'] + '_' + sighting2['longitude']
  
  return isLongestLocation(coors2, coors1)
