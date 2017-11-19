# read contents from one file and copy to other . source and destination files need to be passed as command line arguments

from sys import argv

script,source_file,destination_file = argv

print(f"The source file entered is {source_file}")

open_file_1 = open(source_file)

file1_content = open_file_1.read()

open_file_2 = open(destination_file,'w')

open_file_2.write(file1_content)

open_file_2.close()

open_file_2_again = open(destination_file)

print(f"\n Checking whether content actually got written? Here are the file contents -----> \n {open_file_2_again.read()}")

open_file_2_again.close()









