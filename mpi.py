# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:12:34 2021

@author: Autantic
"""

import mpi4py as MPI
#--- Utilisation de de la bibliothèque openMPI 
#pour une communication point à point

import numpy

# calul du fibonacci de n

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

liste = []
n = int(input("Un nombre: "))

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [liste.append(fibonacci(i)) for i in range(n)]
    comm.Send([data, MPI.INT], dest = 1, tag = 55)
    print(f"process{rank}: {liste}")
elif rank == 1:
    data = comm.Recv(source = 0, tag = 55)
    print(f"process {rank}: {liste}")