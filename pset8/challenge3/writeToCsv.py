import csv

lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=",")
    for list in lists:
        writer.writerow(list)