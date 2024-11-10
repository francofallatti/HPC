#!/usr/bin/env python3
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
numprocs = comm.Get_size()

s = 0.0
h = np.zeros(1)
n = np.zeros(1, dtype=int)

if rank == 0:
    with open("pi.dat") as f:
        n[0] = int(f.readline())
    h[0] = 1.0 / n[0]

comm.Bcast(n, root=0)

for i in range(rank, n[0], numprocs):
    x = (i + 0.5) * h[0]
    s += 4.0 / (1.0 + x * x)

total_s = comm.reduce(s, op=MPI.SUM, root=0)

if rank == 0:
    pi = h[0] * total_s
    print(f"Value of n is {n[0]}")
    print(f"Value of pi is {pi:.12f}")
