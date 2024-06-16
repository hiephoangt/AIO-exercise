def factorial_of_number(y):
    var = 1
    while(y > 1):
        var = var * y
        y = y - 1
    return var

if __name__ == '__main__':
    assert factorial_of_number(8) == 40320
    print(factorial_of_number(4))