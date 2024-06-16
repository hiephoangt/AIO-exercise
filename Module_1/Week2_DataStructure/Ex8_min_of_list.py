def min_of_list(n):
    min_list = n[0]
    for i in range(1, len(n)):
        if n[i] < min_list:
            min_list = n[i]
    return min_list


if __name__ == '__main__':
    my_list = [1, 2, 3, -1]
    print(min_of_list(my_list))
