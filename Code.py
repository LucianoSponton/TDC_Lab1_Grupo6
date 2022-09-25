# *** CircuitPython Grupo 6 *** #

import time
import board
import digitalio


buzzer = digitalio.DigitalInOut(board.GP0)
buzzer.direction = digitalio.Direction.OUTPUT
 
######### Esto es para manejar 1 sensor infrarojo #########  

sensor = digitalio.DigitalInOut(board.GP20)
sensor.direction = digitalio.Direction.INPUT
######### ######### ######### ######### #########  

######### Esto es para manejar 1 led comun de 2 patitas #########  
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT
######### ######### ######### ######### #########  s

######### Esto es para manejar 1 display #########  
seg1 = digitalio.DigitalInOut(board.GP1)
seg2 = digitalio.DigitalInOut(board.GP2)
seg3 = digitalio.DigitalInOut(board.GP3)
seg4 = digitalio.DigitalInOut(board.GP4)
seg5 = digitalio.DigitalInOut(board.GP16)
seg6 = digitalio.DigitalInOut(board.GP17)
seg7 = digitalio.DigitalInOut(board.GP18)

seg1.direction = digitalio.Direction.OUTPUT
seg2.direction = digitalio.Direction.OUTPUT
seg3.direction = digitalio.Direction.OUTPUT
seg4.direction = digitalio.Direction.OUTPUT
seg5.direction = digitalio.Direction.OUTPUT
seg6.direction = digitalio.Direction.OUTPUT
seg7.direction = digitalio.Direction.OUTPUT
######### ######### ######### ######### #########  

######### Esto es para el LED RGB #########  
led_r = digitalio.DigitalInOut(board.GP13)
led_r.direction = digitalio.Direction.OUTPUT

led_g = digitalio.DigitalInOut(board.GP14)
led_g.direction = digitalio.Direction.OUTPUT

led_b = digitalio.DigitalInOut(board.GP15)
led_b.direction = digitalio.Direction.OUTPUT
######### ######### ######### ######### #########  

######### Metodos para prender numeros en display #########  
def Apagar_7Segmentos():
  seg1.value = True
  seg2.value = True  
  seg3.value = True
  seg4.value = True
  seg5.value = True
  seg6.value = True
  seg7.value = True

def Numero_0():
  seg1.value = True
  seg2.value = False  
  seg3.value = False
  seg4.value = False
  seg5.value = False
  seg6.value = False
  seg7.value = False

def Numero_1():
  seg1.value = True
  seg2.value = True  
  seg3.value = True
  seg4.value = False
  seg5.value = False
  seg6.value = True
  seg7.value = True

def Numero_2():
  seg1.value = False
  seg2.value = True  
  seg3.value = False
  seg4.value = False
  seg5.value = True
  seg6.value = False
  seg7.value = False

def Numero_3():
  seg1.value = False
  seg2.value = True  
  seg3.value = False
  seg4.value = False
  seg5.value = False
  seg6.value = False
  seg7.value = True

def Numero_4():
  seg1.value = False
  seg2.value = False  
  seg3.value = True
  seg4.value = False
  seg5.value = False
  seg6.value = True
  seg7.value = True

def Numero_5():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = True
  seg5.value = False
  seg6.value = False
  seg7.value = True

def Numero_6():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = True
  seg5.value = False
  seg6.value = False
  seg7.value = False

def Numero_7():
  seg1.value = True
  seg2.value = True  
  seg3.value = False
  seg4.value = False
  seg5.value = False
  seg6.value = True
  seg7.value = True

def Numero_8():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = False
  seg5.value = False
  seg6.value = False
  seg7.value = False

def Numero_9():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = False
  seg5.value = False
  seg6.value = False
  seg7.value = True
######### ######### ######### ######### #########  

def Letra_E():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = True
  seg5.value = True
  seg6.value = False
  seg7.value = False

def Letra_F():
  seg1.value = False
  seg2.value = False  
  seg3.value = False
  seg4.value = True
  seg5.value = True
  seg6.value = True
  seg7.value = False

######### Metodos para Apagar y Prender el LEDs RGB #########  
def ApagarLeds():
  led_r.value = False
  led_g.value = False
  led_b.value = False

def Prender_Azul():
  led_r.value = True
  led_g.value = False
  led_b.value = False

def Prender_Verde():
  led_r.value = False
  led_g.value = True
  led_b.value = False

def Prender_Rojo():
  led_r.value = False
  led_g.value = False
  led_b.value = True

def Prender_Rosado():
  led_r.value = True
  led_g.value = False
  led_b.value = True

def Prender_Amarillo():
  led_r.value = False
  led_g.value = True
  led_b.value = True
######### ######### ######### ######### #########  

def Prender_Numero(numero): 
  if numero == 0:
    Numero_0()
  elif numero == 1:
    Numero_1()
  elif numero == 2:
    Numero_2()
  elif numero == 3:
    Numero_3()
  elif numero == 4:
    Numero_4()
  elif numero == 5:
    Numero_5()
  elif numero == 6:
    Numero_6()
  elif numero == 7:
    Numero_7()
  elif numero == 8:
    Numero_8()
  elif numero == 9:
    Numero_9()

def Prender_Buzzer():
  buzzer.value = 1 
  time.sleep(0.01)
  buzzer.value = 0 

def Funcion_1():
  
  Apagar_7Segmentos()
  Prender_Numero(0)
  cont = 0
  contador_de_objetos = 0  
  contador_lapso_de_tiempo = 0
  seguir_ejecutando = True
  estado_de_finalizacion = "x"
  No_se_detecto_ninguno_en_5_segundos = False

  while (seguir_ejecutando):
    while sensor.value == 1:
      Prender_Azul()
      buzzer.value = 0 
      time.sleep(0.01)
      cont += 1
      if cont == 500:
        seguir_ejecutando = False
        break
    buzzer.value = 1
    if cont < 500:
      cont = 0
      Prender_Rosado()
      contador_de_objetos += 1
      Prender_Numero(contador_de_objetos)
      time.sleep(0.3)
      if contador_de_objetos == 9:
        estado_de_finalizacion = "ConteoExitoso"
        seguir_ejecutando = False


  if estado_de_finalizacion == "ConteoExitoso":
    buzzer.value = 0 
    ApagarLeds()
    Prender_Verde()
    Letra_E()
    time.sleep(7) # Exito
    print("Conteo Exitoso")
  else:
    ApagarLeds()
    Prender_Rojo()
    Letra_F() # Fracaso
    time.sleep(7)
    print("Conteo Fallido")

def Funcion_2():
  
  Apagar_7Segmentos()
  Prender_Numero(0)
  cont = 0
  contador_de_objetos = 0  
  contador_lapso_de_tiempo = 0
  seguir_ejecutando = True
  estado_de_finalizacion = "x"
  No_se_detecto_ninguno_en_5_segundos = False

  while (seguir_ejecutando):
    while sensor.value == 1:
      Prender_Azul()
      time.sleep(0.01)
      cont += 1
      if cont == 500:
        seguir_ejecutando = False
        break
    if cont < 500:
      cont = 0
      Prender_Rosado()
      contador_de_objetos += 1
      Prender_Numero(contador_de_objetos)
      time.sleep(0.3)
      if contador_de_objetos == 9:
        estado_de_finalizacion = "ConteoExitoso"
        seguir_ejecutando = False


  if estado_de_finalizacion == "ConteoExitoso":
    ApagarLeds()
    Prender_Verde()
    Letra_E()
    time.sleep(7) # Exito
    print("Conteo Exitoso")
  else:
    buzzer.value = 1

    ApagarLeds()
    Prender_Rojo()
    Letra_F() # Fracaso
    time.sleep(7)
    print("Conteo Fallido")
######### Aca inicia el codigo principal #########



Funcion_1()
#Funcion_2()
