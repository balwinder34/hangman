answer= input("What is your name?:")

with open("ans.txt", "w") as f:
    f.write(answer)
#the answer is a variable storing the input
