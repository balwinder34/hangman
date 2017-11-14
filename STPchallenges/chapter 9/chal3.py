import csv
movies= [["Top Gun", "Risky Buisness", "Minority Report"],
["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("mov.csv","w") as f:
    w= csv.writer(f,delimiter=",")
    w.writerow(movies[0])
    w.writerow(movies[1])
    w.writerow(movies[2])
