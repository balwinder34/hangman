list1=[1,10,100,1000]


while True:
    a= input("Guess a number or type 'q' to quit:")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
        print("please ONLY type a number or q to quit.")
    if a in list1:
        print("You guessed it correctly!")
    else:
        print("Try again")
