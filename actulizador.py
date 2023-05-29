import datetime
import os
import time
import sys
from colores import colorverde,colorazul,colorclasic,colormorado,colornaraja,coloramarillo
import random
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'
def banner():
 os.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗  ██╗██████╗ ██╗██████╗
██╔════ ██╔════╝████╗ ██║██╔══██╗██║██╔══██╗
█████╗  █████╗  ██╔██╗██║██████╔╝██║██████╔╝
██╔══   ██╔══╝  ██║╚████║██╔══██╗██║██╔══██╗
██║     ███████╗██║ ╚███║██║  ██║██║██║  ██║
╚═╝     ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝{color.fin}""")
def version():
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.2                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """ 

 suerte = random.randint(0,5)
 if suerte == 0:
   coloramarillo(texto)
 elif suerte == 1:
   colorazul(texto)
 elif suerte == 2 :
   colorclasic(texto)
 elif suerte == 3 :
   colormorado(texto)
 elif suerte == 4 :
   colornaraja(texto)
 elif suerte == 5:
   colorverde(texto)      

fecha_actual = datetime.date.today()

archivo = open("fecha.txt", "r")
hoy = archivo.read()
archivo.close()




if hoy != str(fecha_actual):
    banner()
    version()
    print(f"{color.verde}")
    palabra = "actualizando........"
    time.sleep(0.5)
    for letra in palabra:
     sys.stdout.write(letra)
     sys.stdout.flush()
     time.sleep(0.5)
    print(f"{color.fin}")
    os.system('pkg update -y && pkg upgrade -y')
    fecha_actual_str = str(fecha_actual)
    archivo = open("fecha.txt", "w")
    archivo.write(fecha_actual_str)
    archivo.close()
    banner()
    version()
    print(f"{color.verde}actulizado correctamente{color.fin}")

