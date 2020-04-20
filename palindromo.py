#!/usr/bin/env python
# -*- coding: latin1 -*-

import sys
import unicodedata
import time

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s

f= open("inputPruebas.txt","r")
g = open("outputPruebas.txt","w")

id = 0
for linea in f:
    id = id + 1
    palindromo = "si"           
    frase = elimina_tildes(linea.decode("utf-8").lower().strip())   #preparar String

    largo = (len(frase))            # obtener largo string
    j = 1                           # contador inverso

    # caso caracter unico / caracter vacio / cadena vacia
    if largo == 1 or largo == 0:    
        palindromo = "no"

    for i in range (0,largo):   # Recorrer frase

        # saltar caracteres especiales en contadores i,j
        if frase[i] != " " and frase[i] != "." and frase[i] != "-" and frase[i] != "[" and frase[i] != "]" and frase[i] != ","  and frase[i] != "¿".decode("utf-8") and frase[i] != "?".decode("utf-8") and frase[i] != "¡".decode("utf-8") and frase[i] != "!".decode("utf-8"):         # saltar caracter vacios contador i
            while frase[-j] == " " or frase[-j] == "." or frase[-j] == "-" or frase[-j] == "[" or frase[-j] == "]" or frase[-j] == "," or frase[-j] == "¿".decode("utf-8") or frase[-j] == "?".decode("utf-8") or frase[-j] == "¡".decode("utf-8") or frase[-j] == "!".decode("utf-8"): 
                j = j + 1           

            # comienzo caso \n
            if frase[i] == "\\" and frase[i+1] == "n":
                i = i + 2
                break
            if frase[-j] == "n" and frase[-j-1] == "\\":
                j = j + 2
            #volver a chekear en caso de \n
            while frase[-j] == " " or frase[-j] == "." or frase[-j] == "-" or frase[-j] == "[" or frase[-j] == "]" or frase[-j] == "," or frase[-j] == "¿".decode("utf-8") or frase[-j] == "?".decode("utf-8") or frase[-j] == "¡".decode("utf-8") or frase[-j] == "!".decode("utf-8"): 
                j = j + 1           
            # Fin caso \n
                        
            if frase[i] != frase[-j]:       # Comparar caracteres
                palindromo = "no"
                break
            j = j + 1   

    # Obtener tiempo y fecha actual
    tiempo = time.strftime("%H:%M:%S")
    fecha = time.strftime("%d/%m/%y")

    # Escribir archivo de salida
    g.write("[" + fecha + " " + tiempo + "] Caso de prueba id " + str(id) + " - Resultado: " + palindromo + "\n")

f.close()
g.close()