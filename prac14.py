from itertools import product
A=map(int,input().split())
B=map(int,input().split())
output=list(product(A,B))
for i in output:
    print(i,end=" ")