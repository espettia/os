import threading as th
import random as rand
import time

def A():    
    while True:
        r = rand.randint(1,50)
        time.sleep(r/100)
        print('A',end=' ',flush=True)        

def B():    
    while True:
        r = rand.randint(1,50)
        time.sleep(r/100)
        print('B',end=' ',flush=True)
                 
def C():    
    while True:
        r = rand.randint(1,50)
        time.sleep(r/100) 
        print('C',end=' ',flush=True)        
        
def D():    
    while True:
        r = rand.randint(1,50)
        time.sleep(r/100)
        print('D',end=' ',flush=True)      

if __name__ == "__main__":

    t = []
    h1=th.Thread(target=A)
    t.append(h1)
    h2=th.Thread(target=B)
    t.append(h2)
    h3=th.Thread(target=C)
    t.append(h3)
    h4=th.Thread(target=D)
    t.append(h4)
        
    lista = rand.sample(range(4),4)
    for i in lista:
        t[i].start()
    
    
      
    
