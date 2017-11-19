
#import the argv method from the sys module
from sys import argv

#declare the expected command line arguments
script,first_var,second_var,third_var = argv
print("The script using which the program was run" , script)
print("The first argument passed was",first_var)
#print the lenght of the number of arguments
print(f"The total number of arguments is {len(argv)}")
#print the array of script and argument recieved on the command line
print(argv)

#another way to write the above is to just import sys and use sys.argv in the code to call the argv method. Clearly this is inefficient 

import sys

#declare the expected command line arguments
script,first_var,second_var,third_var = sys.argv
print("The script using which the program was run" , script)
print("The first argument passed was",first_var)
#print the lenght of the number of arguments
print(f"The total number of arguments is {len(sys.argv)}")
#print the array of script and argument recieved on the command line
print(sys.argv)



