#print an alphabetically sorted list of all functions in the re module , which contain the word "find"

import re

list_fnc = []
for i in dir(re):
    if "find" in i:
        list_fnc.append(i)
list_fnc.sort()
#print (list_fnc)
for element in list_fnc:
    print(element)
    

    