import os
import sys 

'''Script to generate a .sh file to copy the desired files including
the md5 checksum in their names to the destiny path'''

def main():

    file_n = open(sys.argv[1], 'r') #list with the files (including root path)
    dest_root = sys.argv[2] #root path to the dest dir

    command_line = """#!/bin/bash
#SBATCH --time=02:00:00
#SBATCH --account=
#SBATCH --cpus-per-task=1
#SBATCH --mem=5G
#SBATCH --mail-user=frog2901@usherbrooke.ca
#SBATCH --mail-type=FAIL
#SBATCH --output=%j-%x.slurm
#SBATCH --job-name=""" + "copy_dup_batch\n\n"

    print(command_line)

    for path in file_n:

        path = path.strip()
        root_path = os.path.dirname(path)
        name = os.path.basename(path)
        new_name = name + '.md5'   
        new_path = os.path.join(root_path,new_name)

        md5_name = open(new_path, 'r')

        for line in md5_name:

            line = line.strip()
            md5,src = line.split('  ')
            name_to_copy = name.split('_')[0] +'-' + md5 + '-raw'
            dest = os.path.join(dest_root,name_to_copy)

            print("cp " + src + " " + dest + "\n") 


if __name__ == "__main__":

    main()







