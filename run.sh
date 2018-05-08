#!/bin/sh

#SBATCH -n 4
#SBATCH -t 5:00:00
#SBATCH --mem=16G
#SBATCH--mail-type=

module load python
python one_thread.py 