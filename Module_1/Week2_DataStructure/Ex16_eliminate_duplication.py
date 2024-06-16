def eliminate_duplication_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def eliminate_duplication(data):
    res = []
    for i in data:
        if eliminate_duplication_helper(i, res):
            res.append(i)
    return res


if __name__ == '__main__':
    lst = [10, 10, 9, 7, 7]
    assert eliminate_duplication(lst) == [10, 9, 7]

    lst = [9, 9, 8, 1, 1]
    print(eliminate_duplication(lst))
