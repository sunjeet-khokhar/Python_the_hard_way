def print_something(*args):
    #arg1,arg2 = args
    #print(f"first argument passed was{arg1} and the second argument passed was{arg2}")
    
    #print all the arguments recieved in the method call , *args means the method can recieved any number of arguments
    for ar in args:
        print(ar+1)
    

for i in range(1,1000):
    print_something(i)
    
#can pass no arguments at all , as well , magic due to *args
print_something()


    
# Task 1 write two methods one two read and print the whole file in one go and another one to read and print the first n lines of the file ,
# with n passed as an argument
# Task 2 when you cread the whole file check whether a particular word exists in the file , if yes print a confirmatory message and if not print a negatory message

file_path = "file_to_read.txt"

def print_whole_file(file_name):
    file_contents = open(file_name).read()
    print(file_contents)
    if ("Wonder" in file_contents):
        print("Yes, the word wonder exists in this file")
    else:
        print("Nope, no wonder here")
    open(file_name).close()
  
    
    
print_whole_file("file_to_read.txt")

def print_first_x_lines(file_name,x):
    file_contents = open(file_name)
    for i in range(2):
        print(file_contents.readline())
    file_contents.close()
        
print_first_x_lines(file_path,2)


#make a function return something 

def divide(a,b):
    return (a/b)

print(f"The quotient after this division operation is {divide(50,5)}")
        

    
