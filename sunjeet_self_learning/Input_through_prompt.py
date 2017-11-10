from sys import argv

prompt_symbol = '>'

script,user = argv 


print(f"Hi {user}")

print("Can I ask you a question?")

print("What is the current computer that you are using?")

computer_model = input(prompt_symbol)

print(f"""
{user} is using {computer_model}
maybe time for a change!
""")



