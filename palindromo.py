#!/usr/bin/env python
# -*- coding: latin1 -*-

import sys
import unicodedata

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s

f= open("inputPruebas.txt","r")
g = open("destino.txt","w")

for linea in f:
    palindromo = "si"
    frase = elimina_tildes(linea.decode("utf-8").lower().strip())

    largo = (len(frase))          # obtener largo string
    j = 1                       # contador inverso
    if largo == 1 or largo == 0:    # caso caracter unico / caracter vacio / cadena vacia
        palindromo = "no"

    for i in range (0,largo):   # Recorrer frase

        if frase[i] != " " and frase[i] != "." and frase[i] != "-" and frase[i] != "[" and frase[i] != "]" and frase[i] != "," and frase[i] != "\\" and frase[i] != "¿".decode("utf-8") and frase[i] != "?".decode("utf-8") and frase[i] != "¡".decode("utf-8") and frase[i] != "!".decode("utf-8"):         # saltar caracter vacios contador i
            if frase[i] == "n" and frase[i+1] == "\\":
                i = i + 2
            if frase[-j] == "n" and frase[-j-1] == "\\":
                j = j + 2

            while frase[-j] == " " or frase[-j] == "." or frase[-j] == "-" or frase[-j] == "[" or frase[-j] == "]" or frase[-j] == ","or frase[-j] == "\\" or frase[-j] == "¿".decode("utf-8") or frase[-j] == "?".decode("utf-8") or frase[-j] == "¡".decode("utf-8") or frase[-j] == "!".decode("utf-8"): 
                j = j + 1           # saltar caracter vacios contador j

            #print(frase[i] + " --> " + frase[-j])
            if frase[i] != frase[-j]:   #comparar caracteres
                palindromo = "no"
                break
            j = j + 1

    print(frase + " --> " + palindromo)
#    print("-------------------------------------")

f.close()
g.close()