dict1={ 
        "sandeep":123,
        "other" : "hey",
        "less": "sucks"



}
dict2={
        "solanki":123
}
for i in dict1:
    for j in dict2:
        if dict2[j]==dict1[i]:
            print("yes")
        else:
            print("no")
            

