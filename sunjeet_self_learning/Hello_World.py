print("Hello from the IDE dchdcdjjdjjdj")
print("1234567\n3437898")
print ('I "got" you man, youdont have to yell')
print ("I \"got\" you man, you dont have to yell")
print ('Let\'s learn Python')
print("Let's learn Python")

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

#some more escape sequences practice 
print("""
Let's practice everything
You'd need to know 'bout escapes with \ that do:
\n
\t
cursour should have inserted a new line and tab here
""")

#as a single line using string literals
print(" You\'d need to know \'bout escapes with \\ that do:")

print("Donald Trump believes he is \"politically\" incorrect, I just think he is \"correctly\" stupid")


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
	
	
