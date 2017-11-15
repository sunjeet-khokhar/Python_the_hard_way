# read contents from one file and copy to other 

from sys import argv

script,source_file,destination_file = argv

print(f"The source file entered is {source_file}")

open_file_1 = open(source_file)

file1_content = open_file_1.read()

open_file_2 = open(destination_file,'w')

open_file_2.write(file1_content)

open_file_2.close()

open_file_2_again = open(destination_file)

print(f"Checking whether content actually got written? {open_file_2_again.read()}")

open_file_1.close()










