def f(x, y, z, c = "ottawa", p = "ontario"):
    """
    three required variables two optional
    """
    sum = x + y + z
    print(sum)
    print(f"{c}, {p}" )

f(2, 4, 6)
f(3, 6, 9, 'middle of', 'nowhere')