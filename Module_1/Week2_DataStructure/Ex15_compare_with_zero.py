def compare_with_zero(num):
    if num  > 0:
        return "T"
    else:
        return "N"

def list_compare_with_zero(numlist):
    res = [compare_with_zero(i) for i in numlist]
    return res

if __name__ == '__main__':
    data = [10 , 0 , -10 , -1]
    assert list_compare_with_zero(data) == ['T', 'N', 'N', 'N']

    data = [2 , 3 , 5 , -1]
    print(list_compare_with_zero(data))