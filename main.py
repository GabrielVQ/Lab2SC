# coding=utf-8

from time import time
from recursos.funciones import *
opcion = -1
while opcion != 3:
    print"Menú"
    print"Escoja una opción:"
    print"1.Encriptar"
    print"2.Descencriptar"
    print"3.Salir"
    opcion = raw_input()
    if opcion == '1':
        print "Ingrese clave encriptación:"
        claveEncriptacion = raw_input()
        print "Ingrese texto:"
        textoPlano = raw_input()
        matriz = matrizClave(claveEncriptacion)
        textoCifrado = encriptar(textoPlano, matriz)
        tiempo_inicial= time()
        print"Texto cifrado:", encriptar(textoPlano, matriz)
        tiempo_final = time()
        tiempo_ejecucion = (tiempo_final - tiempo_inicial) *1000
        print tiempo_ejecucion, "milisegundos"
    if opcion == '2':
        print "Ingrese clave desencriptación"
        claveDesencriptacion = raw_input()
        print "Ingrese texto:"
        #textoCifrado = raw_input()
        matriz = matrizClave(claveDesencriptacion)
        print "Texto plano:", desencriptar(textoCifrado, matriz)