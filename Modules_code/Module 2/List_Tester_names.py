# A list of some of our Testers in the practice. Add more name to reflect the whole Practice !
tester_names = ['Stan' , 'Arpan', 'Christina','Ryan']
#sort the list alphabetically
tester_names.sort()
# print the sorted list 
print(tester_names)

#create a new list
new_list = []
#cherry pick Meridian testers index from the sorted list
for i in [0,2]:
        new_list.append(tester_names[i])
print(f"The Testers working @ Meridian are {new_list}")

