import os
import csv
from colorama import Fore
import time
import datetime
from playsound import playsound
 
 
def check_ping(hostname):
    response = os.system("fping -r 10 -q " + hostname + " >/dev/null")
    if response == 0:
        check_ping = "[OK]"
    else:
        check_ping = "[Error]"
 
    return check_ping
 
 
def sonido_alerta():
   #os.system("play -q red-alert.mp3")
   playsound('C:/Users/User/Documents/script/red-alert.mp3')
 
# Lee los datos del archivo y los guarda en una variable.
archivo_servidores = open('servidores.csv')
servidores_reader = csv.reader(archivo_servidores)
datos_servidores = list(servidores_reader)
 
# Prueba si hay conexión en todos los servidores
contador = 0
 
while True:
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_ping(datos_servidores[i][1])
 
        if resultado == "[Error]":
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.RED + resultado))
            sonido_alerta()
        else:
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.GREEN + resultado))
 
    contador += 1
    print(Fore.BLUE)
    print('{0} {1:%H:%M:%S} {2}'.format(contador, datetime.datetime.now(),
                                    "________________________________________"))
    print()
 
    # Pausa de 10 minutos.
    time.sleep(10)