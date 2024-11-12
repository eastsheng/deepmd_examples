#!/bin/bash
#SBATCH -J dpgen
#SBATCH -N 1
#SBATCH -n 28
#SBATCH --ntasks-per-node=28
#SBATCH --partition=normal,normal2,normal3,normal4
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#export PATH=/data/app/lammps/2023/lammps-2Aug2023/src:$PATH
#export PATH=/data/home/chendongsheng/softwares/lammps/lammps-2Aug2023/src:$PATH
export PATH=/data/home/chendongsheng/softwares/deepmd/deepmd-kit/bin:$PATH
export PATH=/data/app/vasp.6.4.2/bin:$PATH
export GCC_PATH=/data/app/gcc13.2.0
export PATH=/data/app/gcc13.2.0/bin:$PATH
export LD_LIBRARY_PATH=/data/app/gcc13.2.0/lib:/data/app/gcc13.2.0/lib64:$LD_LIBRARY_PATH
source /data/app/intel/bin/compilervars.sh intel64
conda activate base
#ulimit -l unlimited
#ulimit -s unlimited
#NP=$(srun hostname -s |wc -l)
# mpirun -np $NP lmp_mpi -i in.lammps 2>&1 | tee out.$SLURM_JOBID.log
dpgen init_bulk param.json machine.json