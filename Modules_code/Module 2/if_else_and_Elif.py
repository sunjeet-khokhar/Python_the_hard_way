# a simple and easy if else loop
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Elif example
name = 'Dracula'
age = 4000000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age < 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age < 100:
    print('You are not Alice, grannie.')
else:
    print ("you are a perpetual zombie and you are stuck in the else condition of this loop") 
    
# Exercise :: Play around with the value of age to get every print statement printed 
