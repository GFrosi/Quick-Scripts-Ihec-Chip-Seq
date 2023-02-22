import shutil
import os
import sys


"create dir chuncks"

def create_dir(path):
    try:
        os.mkdir(path)
        print("Directory {} created".format(path))
    except OSError:
        print("Directory {} failed".format(path))



def main():
    root_path = sys.argv[1] #root path to GSE directories
    prefix_dir = 'lift_'
    counter = 0
    list_file = os.listdir(root_path)
    path = os.path.join(root_path, prefix_dir + str(counter))

    for index, lift in enumerate(list_file):
        if index % 20 == 0:
            counter += 1
            path = os.path.join(root_path, prefix_dir + str(counter))
            create_dir(path)

if __name__ == "__main__":
    main()
