def merge_the_tools(string, k):
    temp=[]
    len_string=0
    for item in string:
        len_string+=1
        if item not in temp:
            temp.append(item)
        if len_string==k:
            print(''.join(temp))
            temp=[]
            len_string=0
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)