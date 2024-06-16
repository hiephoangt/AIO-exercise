def max_of_list(n):
    max_list = n[0]
    for i in range(1, len(n)):
        if n[i] > max_list:
            max_list = n[i]
    return max_list


if __name__ == '__main__':
    my_list = [1001, 9, 100, 0]
    assert max_of_list(my_list) == 1001

    my_list = [1, 9, 9, 0]
    print(max_of_list(my_list))
