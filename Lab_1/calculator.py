# Sums two numbers
def sum(a, b):
    while a != 0:
        if a > 0:
            a = a - 1
            b = b + 1
        else:
            a = a + 1
            b = b - 1
    return b

# Divides two numbers
def divide(a, b):

    if b == 0:
        raise ValueError('Cannot divide by zero')

    result = 0
    while a != 0:
        result = result + 1
        if b > 0:
            if a > 0:
                a = a - b
            else:
                a = a + b
        else:
            if a > 0:
                a = a + b
            else:
                a = a - b
    return result