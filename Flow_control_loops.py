name = 'Bob'
if name == 'Alice':
    print('Hi, Alice.')
else:
    print('Hello, stranger.')

#Elif example

name = 'Dracula'
age = 4000000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('Nothing matches the stored age')
    
#Fizz Buzz solution in Python
for i in range(1,100):
    if (i%3 == 0 and i%5 == 0):
        print ("FizzBuzz")
    elif (i%5 == 0):
        print ("Buzz")
    elif (i%3 == 0):
        print ("Fizz")
    else:
        print (i)
    
    

