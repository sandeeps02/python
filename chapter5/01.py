myDict={
    "Fast": "In a Quick Manner",
    "Harry": "A coder",
    "Marks": [45,45,54,54],
    "anotherdict": {'harry':'Player'}
}
# print(myDict['Fast'])
# print(myDict['Harry'])
# print(myDict['Marks'])
print(myDict['anotherdict']['harry'])
print(myDict.items())
print(myDict)
updatedict={
    "Lovish": "Friends"
}
myDict.update(updatedict)
print(myDict)
print(myDict.get(harry1))