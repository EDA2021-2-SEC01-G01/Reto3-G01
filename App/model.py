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

  return database


# Funciones para agregar informacion al catalogo

def addSighting(database, sighting):
  lt.addLast(database['sightings'], sighting)
  updateCityIndex(database['cityIndex'] ,sighting)
  updateDateIndex(database['dateIndex'] ,sighting)
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

# Funciones para creacion de datos

def newDateEntry(sighting):
  entry = lt.newList(datastructure='SINGLE_LINKED')
  lt.addLast(entry, sighting)

  return entry


def newCityEntry(sightingTime, sighting):
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

  ms.sort(cities, sortBySightings)

  listCities = lt.newList('SINGLE_LINKED')

  for i in lt.iterator(cities):
    lt.addLast(listCities, om.valueSet(i))

  return (listCities, sightingsByCity)

# Funciones de comparacion

# Funciones de ordenamiento

def sortBySightings(sighting1, sighting2):
  return om.size(sighting1) > om.size(sighting2)
