#<<Example of a Read, print and close operation>>
#Note - Pass the file name through the command line 

from sys import argv
script, filename = argv
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt.close()

