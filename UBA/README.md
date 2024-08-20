Exercise 1: MPI HELLO WORLD PROGRAM

Create simple MPI hello world program in C, Fortran or Python, use filename “hello-mpi.c” or “hello-mpi.f90” or “hello-mpi.py”, rank 0 should print number of processes and all ranks should print “Hello from X” (X is rank)

Commands:
pip install mpi4py
mpiexec -n 4 python hello-mpi.py

Exercise 2: CALCULATING PI USING MPI COLLECTIVE OPERATIONS
• Parallelize a simple program to determine the value of pi.
• The algorithm suggested here is chosen for its simplicity.
The method evaluates the integral of 4/(1+x*x) between 0 and 1.
• The method is simple: the integral is approximated by a sum of n intervals; the
approximation to the integral in each interval is (1/n)*4/(1+x\*x).
• The master process (rank 0) reads the number of intervals from file; the master
should then broadcast this number to all of the other processes. Each process then
adds up every n'th interval (x = rank/n, rank/n+size/n,...).
• Finally, the sums computed by each process are added together using a reduction.

Commands:
mpiexec -n 4 python hello-mpi.py
