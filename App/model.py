﻿"""
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

  database['cityIndex'] = om.newMap(omaptype='RBT')

  database['dateIndex'] = om.newMap(omaptype='RBT')

  return database


# Funciones para agregar informacion al catalogo

def addSighting(database, sighting):
  updateCityIndex(database['cityIndex'] ,sighting)
  updateDateIndex(database['dateIndex'] ,sighting)
  return database

def updateDateIndex(map, sighting):
  sightingTime = dt.strptime(sighting['datetime'], '%Y-%m-%d %H:%M:%S')
  entry = om.get(map, sightingTime.date())

  if entry is None:
    dateEntry = newDataEntry(sighting)
    om.put(map, sightingTime.date(), dateEntry)
  else:
    dateEntry = me.getValue(entry)


def updateCityIndex(map, sighting):
  sightingCityKey = newCityKey(sighting['city'])
  entry = om.get(map, sightingCityKey)

  if entry is None:
    cityEntry = newDataEntry(sighting)
    om.put(map, sightingCityKey, cityEntry)
  else:
    cityEntry = me.getValue(entry)

# Funciones para creacion de datos

def newDataEntry(sighting):
  entry = lt.newList(datastructure='SINGLE_LINKED')
  lt.addLast(entry, sighting)

  return entry


def newCityKey(city):
  key = ''

  for i in city:
    key += str(ord(i))

  return int(key)

# Funciones de consulta

# Funciones de comparacion

# Funciones de ordenamiento
