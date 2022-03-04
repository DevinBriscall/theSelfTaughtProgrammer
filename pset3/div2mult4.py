def div_two(x):
    """
    takes a number as input and divides it by two
    """
    x /= 2
    print(x)
    return x

def mult_four(x):
    """
    takes a number as input and multiplies it by four
    """
    x *= 4
    print(x)
    return x

x = 4;
mult_four(div_two(x))