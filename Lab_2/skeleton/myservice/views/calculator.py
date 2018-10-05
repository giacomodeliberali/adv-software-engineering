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
        raise ZeroDivisionError('Cannot divide by zero')

    isNegativeResult = a > 0 and b < 0 or a < 0 and b > 0

    a = abs(a)
    b = abs(b)

    result = 0

    while a - b >= 0:
        result = result + 1
        a = a - b

    result = -result if isNegativeResult else result

    return result