from itertools import product
import random
import threading
import multiprocessing
import logging
from threading import Thread
from queue import Queue
import time
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#Função para ajustar os logs
def display(msg):
    thread = threading.current_thread().name
    processo = multiprocessing.current_process().name
    logging.info(f'{processo}\{thread}: {msg}')

#Produtor
def produzir(buffer, semaforo, max):
    semaforo.put(False)
    for x in range(max):
        v = random.randint(1,100)
        buffer.put(v)
        display(f'Produzindo {x}: {v}')
    semaforo.put(True)
    display('Terminou de produzir')

#Consumidor
def consumir(buffer, semaforo):
    counter = 0
    while True:
        if not buffer.empty():
            v = buffer.get()
            display(f'Consumindo {counter}: {v}')
            counter += 1
        else:
            q = semaforo.get()
            if q == True:
                break
        display('Terminou de consumir')

#Main
def main():
    max = 4
    buffer = Queue()
    semaforo = Queue()

    produtor_1 = Thread(target=produzir,args=[buffer, semaforo, max],daemon=True)
    produtor_2 = Thread(target=produzir,args=[buffer, semaforo, max],daemon=True)
    consumidor_1 = Thread(target=consumir,args=[buffer, semaforo],daemon=True)
    consumidor_2 = Thread(target=consumir,args=[buffer, semaforo],daemon=True)

    consumidor_1.start()
    consumidor_2.start()
    
    produtor_1.start()
    produtor_2.start()
    
    consumidor_1.join()
    display('consumidor_1 terminou')

    consumidor_2.join()
    display('consumidor_2 terminou')

    produtor_1.join()
    display('produtor_1 terminou')

    produtor_2.join()
    display('produtor_2 terminou')

    

    display('Fim')

if __name__ == "__main__":
    main()