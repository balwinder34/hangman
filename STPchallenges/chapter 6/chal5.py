l=["The","fox","jumped","over","the","fence","."]

on= " ".join(l)
one= on.replace(" .",".")
print(one)
#my solution

fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
fox = fox[0: -2] + "."
print(fox)
#book solution
