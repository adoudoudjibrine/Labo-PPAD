#Importation du modul multiprocessing
from multiprocessing import Process, Queue

def fil(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__' :
    q = Queue()
    p = Process(target=fil, args=(q,))
    p.start()
    print(q.get())
    p.join()
    