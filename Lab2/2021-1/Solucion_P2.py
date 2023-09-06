from concurrent import futures
import threading as th
import random
import time

numH = 0
numO = 0

def Hidrogeno():
    global numH
    c.acquire()
    while numH == 2:
        c.wait()
    # mantener solo un print
    print("H",end="") 
    numH += 1 
    time.sleep(random.random())           
    c.notifyAll()
    c.release()

def Oxigeno():
    global numO
    c.acquire()
    while numO == 1:
        c.wait()
    # mantener solo un print
    print("O",end="")
    numO += 1
    time.sleep(random.random())   
    c.notifyAll()
    c.release()   

def CambiodeLinea():
    global numH
    global numO
    c.acquire()
    while numH != 2 or numO != 1:
        c.wait()
    # mantener solo un print
    print()
    numH = 0
    numO = 0
    time.sleep(random.random())   
    c.notifyAll()
    c.release()
  
c = th.Condition()  

# No modificar ninguna de las siguientes líneas

with futures.ThreadPoolExecutor(max_workers=40) as executor:
    for _ in range(20):
        executor.submit(Hidrogeno)
    for _ in range(10):
        executor.submit(Oxigeno)
    for _ in range(10):
        executor.submit(CambiodeLinea)
