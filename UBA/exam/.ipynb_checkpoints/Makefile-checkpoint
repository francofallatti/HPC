CC = gcc
MPICC = mpicc
OMPFLAG = -fopenmp
CFLAGS  = -Wall

all: poly-ser poly-mpi poly-omp poly-hyb

poly-ser: poly-ser.c
	$(CC) $(CFLAGS) $< -o $@

poly-mpi: poly-mpi.c
	$(MPICC) $(CFLAGS) $< -o $@

poly-omp: poly-omp.c
	$(CC) $(CFLAGS) $(OMPFLAG) $< -o $@

poly-hyb: poly-hyb.c
	$(MPICC) $(CFLAGS) $(OMPFLAG) $< -o $@

make clean:
	rm -f poly-ser poly-mpi poly-omp poly-hyb
