from lib2to3.pytree import LeafPattern


name= "Mother fucker "
letter=input("Enter what you wanna check:").casefold()
if letter in name.casefold():
    print("yes")
else:
    print("no")
