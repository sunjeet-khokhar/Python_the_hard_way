print ("let me read your name from console")
name = input()
print(f"in case you ever forget your name...here it is ---> {name}" )
# a better way to write the above input prompts is 
name = input("What is your name ?")
print(f"THe name entered was {name}")

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