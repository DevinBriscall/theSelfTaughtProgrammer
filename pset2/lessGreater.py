while True:
    x = input("input a number: ")
    if x.isdigit():
        x = int(x)
        break

if x < 20:
    print("x is less than 20")
elif x > 20:
    print("x is greater than 20")
else:
    print("x is 20")