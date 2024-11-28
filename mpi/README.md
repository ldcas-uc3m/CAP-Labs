# Compilación

Ejemplos compilados a través de CMake:

```
mkdir build
cd build
cmake -DCMAKE_C_COMPILER=mpicc.mpich ..
make
```

# Ejecución

Ejecución de 6 procesos sobre 2 nodos de cómputo en Slurm.

```
srun -N 2 -n 6 --mpi=pmix ./e1-hello_world
```

```
srun --export=OMP_NUM_THREADS=2 -n 2 --mpi=pmix ./e15-hibrido
```


Ejecución sobre un fichero batch en Slurm. Fichero `run.sh`

```
#!/bin/bash
#SBATCH --job-name=trabajo
#SBATCH --output=trabajo_%j.log
#SBATCH --time=00:00:30  # max duration
#SBATCH --ntasks=4  # MPI tasks
#SBATCH --nodes=6  # number of nodes
#SBATCH --cpus-per-task=1  # cpus per task
#SBATCH --partition=all*

srun --mpi=pmix ./e1-hello_world
```


Ejecución:

```
sbatch run.sh
```
