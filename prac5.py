txt = "Japan \\ China \\ Singapore \\ London"
l=txt.split("\\")
c=0
for i in l:
    if(i.find('a')!=-1):
        print(True)