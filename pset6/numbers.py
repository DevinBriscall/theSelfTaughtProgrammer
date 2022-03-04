numbers = ['23','44','55','2','76','32','12','61']
while True:
    print("type 'q' to quit")
    a = input("Guess a number: ")
    if a == 'q':
        break
    if a in numbers:
        print("Good guess!")
    else:
        print("no sorry!")