print("Hello from the IDE dchdcdjjdjjdj")
print("1234567\n3437898")
print ('I "got" you man, youdont have to yell')
print ("I \"got\" you man, you dont have to yell")
print ("Circumference of a circle with a radious of 10 is -->" ,2 * 3.142 * 10)
total_taxis = 100
size = 4
expected_customers = 120
size_without_driver = size - 1
number_of_cars_required = expected_customers/size_without_driver
print(f"number of cars required {number_of_cars_required}")


#print ("let me read your name from console")
#name = input()
#print(f"in case you ever forget your name...here it is ---> {name}" )
# a better way to write the above input prompts is 
#name = input("What is your name ?")
#print(f"THe name entered was {name}")

from sys import argv

script,first_var,second_var,third_var = argv
print("The script using which the program was run" , script)
print("The first argument passed was",first_var)
#print the lenght of the number of arguments
print(len(argv))
#print the array of script and argument recieved on the command line
print(argv)
name=input("What is your name?")
print(f"The name that was input was {name}")