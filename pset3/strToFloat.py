def str_to_float():
    """
    asks user for input and converts it to a float
    """
    
    while True:
        x = input("input a number: ")
        try:
            x = float(x)
            print(x)
            break
        except ValueError:
            print("not a valid number")

str_to_float()