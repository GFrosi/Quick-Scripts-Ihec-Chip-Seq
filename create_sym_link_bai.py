import sys
import subprocess
import os.path
import os


'''This program receives a list of files (including the root path),
a list of numbers (fragment length) and a string to generate symlinks
with a new name.'''


list_of_paths = open(sys.argv[1], 'r') # list of files with root path
list_of_frag = open(sys.argv[2], 'r') # list of numbers


suffix = sys.argv[3] # suffix name of your file (i.e merged.bam)


for line, frag in zip(list_of_paths, list_of_frag):

    line = line.strip()
    fn = os.path.basename(line)
    dir_name = os.path.dirname(line)
    new_fn = fn.replace(suffix,'')
    link = new_fn + "-frag-" + str(frag.strip()) + suffix
    cmd = 'ln -s ' + line + ' ' + os.path.join(dir_name, link)

    subprocess.call(cmd, shell=True)
    #print(cmd)

