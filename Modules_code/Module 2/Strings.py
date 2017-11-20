#strings and some common operations 

name = "Mary had a little lamb"

#this will split the sentence based on whatever is passed on as the argument , a blank space in this case and return a list
name_split = name.split(" ")
print(name_split)

# iterate through the list and print each entry
for word in name_split:
    print(word)

# iterate through the list , and the list method will split each word into letters and return a list
for word in name_split:
    print(list(word))

# joining the sentence back , note that a list has not got a join method that is why we had to use a blank string to invoke the string object and it's join method.
print(" ".join(name_split))

	

