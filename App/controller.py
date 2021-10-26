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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización de la base de datos

def init():
  database = model.newDatabase()
  return database

# Funciones para la carga de datos

def loadData(database, sightingsFile):
  sightingsFile = cf.data_dir + sightingsFile

  inputFile = csv.DictReader(open(sightingsFile, encoding='utf-8'), delimiter=',')
  
  for sighting in inputFile:
    model.addSighting(database, sighting)

  return database

# Funciones de consulta sobre el catálogo

def getOrderedCitiesByCount(database, city):
  cityKey = model.newCityKey(city)
  return model.getOrderedCitiesByCount(database, cityKey)


def getOrderedSightingsByDuration(database, minTime, maxTime):
  return model.getOrderedSightingsByDuration(database, float(maxTime), float(minTime))


def getOrderedSightingsByLocation(database, minLatitude, minLongitude, maxLatitude, maxLongitude):
  minLocation = minLatitude + '_' + minLongitude
  maxLocation = maxLatitude + '_' + maxLongitude

  return model.getOrderedSightingsByLocation(database, minLocation, maxLocation)
