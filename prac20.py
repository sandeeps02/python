from ctypes.wintypes import SIZE

f=[]
x=int(input())
size=list(map(int,input().split()))
n=int(input())
for i in range(1,n+1):
    ni=list(map(int,input().split()))
    if ni[0] in size:
        size.remove(ni[0])
        f.append(ni[1])
print(sum(f)) 


       
