attributes={"height":"5'11",
            "favorite color":"green",
            "favorite author":"Steven King"}

n= input("Ask about my height, favorite color, or favorite author:")
if n in attributes:
    att= attributes[n]
    print (att)
else:
    print("No, you gotta pick from the list, exact typing only")
