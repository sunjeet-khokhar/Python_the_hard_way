#understaning defaultict to use form a dictionary full of lists 

cities = {'San Francisco': 'US', 'London':'UK',
          'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

from collections import defaultdict

d1 = defaultdict(list)
print(d1)
#print(cities.items())

for k,v in cities.items():
    d1[v].append(k)
print(d1)

L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

d2 = defaultdict(list)
print(d2)

for x in L:
    d2[len(str(x))].append(x)
print(d2)