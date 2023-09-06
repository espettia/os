from concurrent import futures
import threading as th
import random
import time

def Hidrogeno():
    for x in range(1,41):
        time.sleep(random.random())
        print("H",end="")

def Oxigeno():
    for y in range(1,21):
        time.sleep(random.random())
        print("O",end="")

def CambiodeLinea():
    for z in range(1,21):
        time.sleep(random.random())
        print()

# No modificar ninguna de las siguientes líneas

with futures.ThreadPoolExecutor(max_workers=3) as executor:    
        executor.submit(Hidrogeno)
        executor.submit(Oxigeno)    
        executor.submit(CambiodeLinea)


