import sys
import os.path

f_input = open(sys.argv[1], 'r')
fraglen = sys.argv[2]

#suffix = ".merged.bam"

command_line = """#!/bin/bash
#SBATCH --time=72:00:00
#SBATCH --account=def-jacquesp
#SBATCH --mem=31G
#SBATCH --cpus-per-task=24
#SBATCH --job-name=""" + "Raw-Bigwig-frag_" + fraglen + "\nmodule load java/1.8 mugqic/deepTools/2.5.3 samtools/1.5\n"

print command_line

for line in f_input:
     
     dir_name = os.path.dirname(line)
     fn = os.path.basename(line.strip())
#     fn = fn.replace(suffix,'')
#     fn = fn + '-frag-' + str(fraglen) + suffix
     fn = os.path.join(dir_name, fn)

     print"\nbash /home/frosig/scratch/chip-seq-ihec-test/singularity-wrapper-encode/integrative_analysis_chip/encode-wrapper/postprocess_downloaded/integrative_analysis_chip/encode-wrapper/postprocess/postprocess.sh " , fn , " " , str(fraglen)  
     
     #print(dir_name)
     #print(fn)
     md5sum_name = os.path.basename(fn).replace('bam','raw.bigwig')
     to_md5sum = os.path.join(dir_name, md5sum_name)
     #print to_md5sum
     out = to_md5sum + ".md5"
     #print "\n",out
     
     print "\nmd5sum", to_md5sum, ">", out   
