def limit_data(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert limit_data(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(limit_data(max=max, min=min, data=my_list))
