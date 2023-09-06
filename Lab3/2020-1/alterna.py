import threading as th
import random as rand
import time

def izq_der():
    r = rand.randint(10,20)
    time.sleep(r/100)
    print("------->", flush=True)
    
def der_izq():
    r = rand.randint(10,20)
    time.sleep(r/100)
    print("<-------", flush=True)
    
ths = []
for i in range(10):
    t = th.Thread(target=izq_der)
    ths.append(t)

for i in range(10):
    t = th.Thread(target=der_izq)
    ths.append(t)

for i in range(20):
    ths[i].start()

for i in range(20):
    ths[i].join()
