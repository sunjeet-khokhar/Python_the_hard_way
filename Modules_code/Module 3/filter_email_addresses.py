# find and print a list of all email addresses starting with '#' 
match = re.findall(r'[\w]+@[.\w]+','xyz #alice123b@google.co.nz purple monkey 123 #sunjeet48484@botbot123.com')
print(match)

