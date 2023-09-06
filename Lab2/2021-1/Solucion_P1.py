from concurrent import futures
import threading as th
import random
import time

def Hidrogeno():
    for x in range(1,41):
        #if(x % 2 == 1 and x != 1): 
        #    boxigeno.wait()    
        #if(x % 2 == 0): 
        #    bhidrogeno.wait()

        time.sleep(random.random())
        print("H",end="")
        #boxigeno.wait()
        bhidrogeno.wait()
        bcambio.wait()

def Oxigeno():
    for y in range(1,21):
        #boxigeno.wait()
        #bhidrogeno.wait()

        time.sleep(random.random())

        while bhidrogeno.n_waiting >= 0:
            if bhidrogeno.n_waiting:
                bhidrogeno.wait()
                bcambio.wait()
                break
        bhidrogeno.wait()       
        print("O",end="")
        boxigeno.wait()
        #boxigeno.wait()
        #bcambio.wait()

def CambiodeLinea():
    for z in range(1,21):
        #bhidrogeno.wait()
        #if z != 20:
        #bcambio.wait()             
        #boxigeno.wait()
       
        time.sleep(random.random())
        boxigeno.wait()
        print()
        bcambio.wait()

boxigeno = th.Barrier(2)
bhidrogeno = th.Barrier(2)
bcambio = th.Barrier(2)

# No modificar ninguna de las siguientes líneas

with futures.ThreadPoolExecutor(max_workers=3) as executor:    
        executor.submit(Hidrogeno)
        executor.submit(Oxigeno)    
        executor.submit(CambiodeLinea)


