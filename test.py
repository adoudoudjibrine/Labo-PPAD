import cPickle
import numpy as np
a = np.linspace(0., 1., 100)
b = "une chaine"
fichier = open("pickleData", "w")
cPickle.dump([a, b], fichier, 0)


from mpi4py import MPI 
comm = MPI.COMM_WORLD 
rank = comm.Get_rank() 
size = comm.Get_size()
print('hello world from process %d/%d' %(rank,size))
