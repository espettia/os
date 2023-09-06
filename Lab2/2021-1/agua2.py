from concurrent import futures
import threading as th
import random
import time


def Hidrogeno():
    time.sleep(random.random())
    # mantener solo un print
    print("H",end="")

def Oxigeno():
    time.sleep(random.random())
    # mantener solo un print
    print("O",end="")    

def CambiodeLinea():
    time.sleep(random.random())
    # mantener solo un print
    print()
    

# No modificar ninguna de las siguientes líneas

with futures.ThreadPoolExecutor(max_workers=40) as executor:
    for _ in range(20):
        executor.submit(Hidrogeno)
    for _ in range(10):
        executor.submit(Oxigeno)
    for _ in range(10):
        executor.submit(CambiodeLinea)

