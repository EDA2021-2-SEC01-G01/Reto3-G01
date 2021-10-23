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
import config as cf
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

  file = files.get(input('> ')[0], None)

  if file is None:
    loadData(database)
  else:
    controller.loadData(database, file)

def printMenu():
  print("Bienvenido")
  print("1- Cargar información en la base de datos")
  print("2- ")

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
    pass
  else:
    sys.exit(0)
sys.exit(0)
