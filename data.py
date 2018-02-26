import re

f=open('test.txt','r')
data=f.read()
data=re.split('<|>' ,data)
final=[]
for i in range(len(data)):
    if i%2 ==0 :
        final.append(data[i])

data=''.join(final)
"""
data=re.split('<a href=|</a>' ,data)
final=[]
for i in range(len(data)):
    if i%2 !=1 :
        final.append(data[i])

data=''.join(final)
"""
data=data.split('\n')
f=open('test.txt','w')
for x in data:
    if len(x) > 0:
        f.write(x)