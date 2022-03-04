import csv
with open("newfile.txt", "w", newline='') as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(['one', 'two', 'three'])
    writer.writerow(['four', 'five', 'six'])

with open("newfile.txt", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(",".join(row))