#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks=128
#SBATCH --output=exam-out.%j
#SBATCH --error=exam-err.%j
#SBATCH --time=00:30:00
#SBATCH --partition=batch
#SBATCH --account=training2427

module purge
module load GCC ParaStationMPI

# Test Serial Execution
echo "Testing Serial Execution"
./poly-ser

# Test MPI Execution on 2, 4, 8, ..., 128 ranks
for ranks in 2 4 8 16 32 64 128; do
    echo "Testing MPI Execution with $ranks ranks"
    srun --ntasks=$ranks ./poly-mpi
done

# Test OpenMP Execution on 2, 4, 8, ..., 128 threads
for threads in 2 4 8 16 32 64 128; do
    echo "Testing OpenMP Execution with $threads threads"
    export OMP_NUM_THREADS=$threads
    ./poly-omp
done

# Test Hybrid Execution on combinations matching total cores
for ranks in 2 4 8 16; do
    for threads in 2 4 8 16; do
        total_cores=$((ranks * threads))
        if [[ $total_cores -eq 128 || $total_cores -eq 256 ]]; then
            echo "Testing Hybrid Execution with $ranks ranks and $threads threads"
            export OMP_NUM_THREADS=$threads
            srun --ntasks=$ranks --cpus-per-task=$threads ./poly-hyb
        fi
    done
done

echo $USER
date
