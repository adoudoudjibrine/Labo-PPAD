#Importation de multiprocessing
from multiprocessing import Process,Pipe

def Pip(conn):
    conn.send([42, None,'Bonsoir'])
    conn.close()

def t(conn):
    conn.send([434, None,'Salut'])
    conn.close()
    
if __name__ == '__main__' :
    parent_con, child_con = Pipe()
    #p = Process(target=Pip, args=(child_con,))
    p = Process(target=t, args=(child_con,))
    p.start()
    print(parent_con.recv())
    p.join()