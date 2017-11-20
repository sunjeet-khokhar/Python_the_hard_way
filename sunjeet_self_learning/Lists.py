# all things lists 

list_names = ['sunj','jeet','kho']
list_names.clear
print(list_names)


spam = ['cat', 'bat', 'rat', 'elephant']
for s in spam:
    print(s)
    
print(spam[0])
print(spam[-1])
print(''.join(spam))
print("#".join(spam[0:4]))
spam.sort()
print(spam)


tester_names = ['Stan' , 'Arpan', 'Christina','Ryan']
tester_names.sort()
print(tester_names)
for i in tester_names:
    if (i=='Arpan'):
        print(i)
    else:
        print("does not exist")
        
new_list = []

for i in [1,3]:
        new_list.append(tester_names[i])
print(new_list)
