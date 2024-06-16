def compare_list_to_number(integers, number = 1):
    result = []
    for i in integers:
        if i == number:
            result.append(True)
        else:
            result.append(False)
    return any(result)

if __name__ == '__main__':
    my_list = [1 , 3 , 9 , 4]
    assert compare_list_to_number(my_list , -1) == False

    my_list = [1 , 2 , 3 , 4]
    print(compare_list_to_number(my_list , 2))