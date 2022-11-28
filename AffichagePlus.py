#Impportation du module multtiprocessing 
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('Module name : ', __name__)
    print('Parent Process : ', os.getppid())
    print('Process id : ', os.getpid())

def f(name):
    info('function f')
    print('Hello', name)
    
if __name__ == '__main__' :
    info('main line')
    p = Process(target=f, args='bob',)
    p.start()
    p.join()
