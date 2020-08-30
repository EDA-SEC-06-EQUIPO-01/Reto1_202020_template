"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

movies_dir = "themoviesdb/"
details = movies_dir + "SmallMoviesDetailsCleaned.csv"
casting = movies_dir + "MoviesCastingRaw-small.csv"

import config as cf
import sys
import csv
import req
import helper as h
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")


def compareRecordIds(recordA, recordB):
    if int(recordA["id"]) == int(recordB["id"]):
        return 0
    elif int(recordA["id"]) > int(recordB["id"]):
        return 1
    return -1


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None
    """

    while True:
        printMenu()  # imprimir el menu de opciones en consola
        # leer opción ingresada
        inputs = input("Seleccione una opción para continuar\n")
        if len(inputs) > 0:

            if int(inputs[0]) == 1:  # opcion 1
                lista_details = h.loadCSVFile(
                    details, impl="ARRAY_LIST", cmpfunction=None
                )
                lista_casting = h.loadCSVFile(
                    casting, impl="ARRAY_LIST", cmpfunction=None
                )

            elif int(inputs[0]) == 2:  # opcion 2
                pass

            elif int(inputs[0]) == 3:  # opcion 3
                director = input("Ingrese el nombre del director\n")
                try:
                    information = req.conocer_director(
                        lista_details, lista_casting, director
                    )
                    for d in information:
                        print(
                            "id:",
                            d["id"],
                            " - " "title:",
                            d["title"],
                            " - ",
                            "vote average:",
                            d["vote_average"],
                        )
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 4:  # opcion 4
                pass

            elif int(inputs[0]) == 5:  # opcion 5
                pass

            elif int(inputs[0]) == 6:  # opcion 6
                print("Que genero quiere para crear el ranking? ")
                g = input()
                print("cuantas entradas quiere? ")
                e = int(input())
                print("De peor a mejor (1) - De mejor a peor (2) ? ")
                e = int(input())
                try:
                    _ = req.crear_ranking_genero(lista_details, e, g, ascendent=True)
                except UnboundLocalError:
                    print("\n" * 10 + "!!!\n\nPrimero carga los datos\n\n!!!")

            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


if __name__ == "__main__":
    main()
