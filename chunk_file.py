import sys

'''script a file to chunck it into several files. 
The chunck will be made each 20 lines'''

f_name = open(sys.argv[1], 'r') #path to file with all paths-to-file to chunk (in this case to liftover)
counter = 0
lines = []

for line in f_name:
    line = line
    lines.append(line)


file_chunks = open("file_chunk_0.txt", 'w') #Open the first output to write the first chunked lines 

for index, ele in enumerate(lines):
    
    if index % 20 == 0:
        counter += 1
        file_chunks.write(ele) #writing the first file
        file_chunks.close()

        file_chunks = open('file_chunk'+ str(counter) + ".txt", 'w') #after the first file, the new ones will be created 
    
    else:

        file_chunks.write(ele)
        
        print(file_chunks, 'created')
        