import numbers
from unicodedata import numeric


number=[3,7,200,300,3001,4001,4007]
minallowed=200
maxallowed=400
start=0
stop=0
# for index in range(len(number)-1,-1,-1):
#     print(number[index],index)
    
for i in range(len(number)-1,-1,-1):
    if number[i]>maxallowed or number[i]<minallowed:
        print(i,number)
        del number[i]

print(number)    