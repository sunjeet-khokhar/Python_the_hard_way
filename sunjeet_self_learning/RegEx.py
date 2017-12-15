import re


# match the pattern iii 
match = re.search('iii','piiig')
print(match.group())   # iii

# . denotes match any character except \n
match = re.search(r'..g','piig')
print(match.group())  #iig

# match three digits in a row 
match = re.search(r'\d\d\d','123')
print(match.group()) 

# match digit character by \d and word characters by \w
match = re.search(r'\w\w\w','%$ab%#abc123')
print(match.group())

match = re.search(r'\d\s?', 'xx1 2 x') # match digit \d and \s - white space character ..... ? indiciates 0 or 1 occurences 
print(match.group())

match = re.search(r'\d\s*', 'xx1 2 x') # match digit \d and \s - white space character ..... ? indiciates 0 or more  
print(match.group())

match = re.search(r'\d\s+', 'xx1 2 xx') # match digit \d and \s - white space character ..... ? indiciates  1 or more occurences 
print(match.group())

match = re.search(r'iiii', 'piigiiiiooooiiii iiiii') 
print(match.group())


match = re.findall(r'iiii', 'piigiiiiooooiiii iiiii ii') 
print(match)

#match = re.search(r'\d\d\d', 'xx1 2   3 xx')
#print(match.group())

match = re.search(r'i?','iiiii')
print(match.group())

# find and print a list of all email addresses starting with '#' 
match = re.findall(r'[\w]+@[\w.]+','xyz #alice123b@google.co.nz purple monkey 123 #sunjeet48484@botbot123.com')
for m in match:
    print(f'The filtered email address is {m}') 

# use round brackets to split the output in groups
match = re.findall(r'([\w]+)@([\w.]+)','xyz #alice123b@google.co.nz purple monkey 123 #sunjeet48484@botbot123.com')
print(match)








