answer = input("what is your phone number? ")

with open("phone-numbers.txt", "w") as file:
    file.write(answer)