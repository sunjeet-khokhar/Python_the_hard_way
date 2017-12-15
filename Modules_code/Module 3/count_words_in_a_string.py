#count the number of times a word appears in a string 

name = '''Peter Piper picked a peck of pickled peppers.
A peck of pickled peppers Peter Piper picked.
If Peter Piper picked a peck of pickled peppers,
Where's the peck of pickled peppers Peter Piper picked? '''

#this will split the sentence based on whatever is passed on as the argument , a blank space in this case and return a list
name_split = name.split(" ")

dict_words = dict()
for i in name_split:
    if i.isalnum():
        if i in dict_words:
            dict_words[i] = dict_words[i]+1
        else:
            dict_words[i] = 1

for key in dict_words.keys():
    print(f"The word \"{key}\" occurs {dict_words[key]} times")
