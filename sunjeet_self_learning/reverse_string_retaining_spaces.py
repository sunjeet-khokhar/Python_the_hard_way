'''
Reverse a string but retain spaces in the same place as the orginal string
'''
s = 'Your code rocks'
list_1 = list(s)
print(list_1)
list_2 = []
for x in range(len(list_1)):
    if list_1[x] == ' ':
        list_2.append(x) 
print(list_2)
list_3 = list(reversed(s.replace(' ','')))
print(list_3)
for x in list_2:
    list_3.insert(x,' ')
print(''.join(list_3))


# best solution from the codewars forum

def solve(s):
    space_index=[i for i in range(len(s)) if s[i]==" "]    #find index of saces  
    s = ''.join(s.split())                                 #remove spaces
    s=s[::-1]                                              #reverse the string    
    for i in space_index:                                  #add spaces again to exactly same place before
        s = s[:i] + " " + s[i:]
    return s


        
        



