# coding=utf-8

from timeit import timeit
def numeroLetra(unicode):
    #Función para convertir un numero a una letra
    #tamaño del alfabeto: 0-300, el resto fue cambiado para poder imprimirlo
    if unicode <= 31 and unicode != 10 or unicode >= 127 and unicode <= 160:
        unicode = 400 + unicode
    letra = unichr(unicode)
    return letra


def letraNumero(letra):
    #Función para convertir una letra en un numero
    #tamaño del alfabeto: 0-300, el resto fue cambiado para poder imprimirlo
    unicode = ord(letra)
    if unicode >= 400:
        unicode = unicode-400
    return unicode


def sumaLetraNumero(texto):
    acumulador = 0
    for i in range(len(texto)):
        acumulador = acumulador + letraNumero(texto[i])
    return acumulador


def matrizClave(clave):
    #Función que genera la matriz de claves
    matriz = []
    for i in range(3):
        matriz.append([0]*3)
    #Se asigna un valor para elemento de la matriz
    matriz[0][0] = len(clave) % 300
    matriz[0][1] = sumaLetraNumero(clave) % 300
    matriz[0][2] = (len(clave) + sumaLetraNumero(clave)) % 300
    matriz[1][0] = abs(len(clave) - sumaLetraNumero(clave)) % 300
    matriz[1][1] = (len(clave) * sumaLetraNumero(clave)) % 300
    matriz[1][2] = (len(clave) * 428) % 300
    matriz[2][0] = (sumaLetraNumero(clave) * 256) % 300
    matriz[2][1] = (sumaLetraNumero(clave) + 26) % 300
    matriz[2][2] = abs(sumaLetraNumero(clave) + 528) % 300

    return matriz


def encriptar(textoPlano, matriz):
    #Funcion de encriptación
    columnaActual = 0
    filaActual = 0
    acumulador = 0
    textoCifrado = ""
    letra = ""
    matrizClave = matriz
    for contador in range(len(textoPlano)):
        if columnaActual == 3:
            filaActual = filaActual + 1
            filaActual = filaActual % 3
            for i in range(3):
                matrizClave[filaActual][i] = matrizClave[filaActual][i] + acumulador #Con esto la salida cambia según la entrada
                matrizClave[filaActual][i] = matrizClave[filaActual][i] % 300
            acumulador = 0
            columnaActual=0
        letra = textoPlano[contador]
        unicode = letraNumero(letra) + matrizClave[filaActual][columnaActual]
        unicode = unicode % 300

        textoCifrado = textoCifrado + numeroLetra(unicode)
        acumulador = acumulador + unicode
        columnaActual = columnaActual + 1

    return textoCifrado


def desencriptar(textoCifrado, matriz):
    # Funcion de desencriptación
    columnaActual = 0
    filaActual = 0
    acumulador = 0
    textoDescifrado = ""
    letra = ""
    matrizClave = matriz
    for contador in range(len(textoCifrado)):

        if columnaActual == 3:
            filaActual = filaActual + 1
            filaActual = filaActual % 3
            for i in range(0, 3, 1):
                matrizClave[filaActual][i] = matrizClave[filaActual][i] + acumulador #Con esto la salida cambia según la entrada
                matrizClave[filaActual][i] = matrizClave[filaActual][i] % 300
            acumulador = 0
            columnaActual = 0
        letra = textoCifrado[contador]
        unicode = letraNumero(letra) - matrizClave[filaActual][columnaActual]

        if unicode < 0:
            unicode = unicode + 300
        unicode = unicode % 300
        textoDescifrado = textoDescifrado + numeroLetra(unicode)
        acumulador = acumulador + letraNumero(letra)
        columnaActual = columnaActual + 1


    return textoDescifrado