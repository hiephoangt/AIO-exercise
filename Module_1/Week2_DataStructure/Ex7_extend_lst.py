def extend_lst(x,y):
    tem = x.copy()
    for i in y:
        tem.append(i)
    return tem

if __name__ == '__main__':
    list_num1 = ['a', 2 , 5]
    list_num2 = [1 , 1]
    list_num3 = [0 , 0]

    assert extend_lst(list_num1 , extend_lst(list_num2 , list_num3)) == ['a', 2 , 5 , 1 , 1 ,0 , 0]

    list_num1 = [1 , 2]
    list_num2 = [3 , 4]
    list_num3 = [0 , 0]

    print(extend_lst(list_num1 , extend_lst(list_num2 , list_num3)))