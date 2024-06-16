def divisible_number(numlist):
    var = []
    for i in numlist:
        if i % 3 == 0:
            var.append(i)
    return var

if __name__ == '__main__':
    assert divisible_number ([3 , 9 , 4 , 5]) == [3 , 9]
    print(divisible_number ([1 , 2 , 3 , 5 , 6]) )