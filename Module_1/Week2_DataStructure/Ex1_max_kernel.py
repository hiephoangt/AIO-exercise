def max_kernel(num_list,windowsize):
    result = []

    for i in range(len(num_list)-windowsize+1):
        result.append(max(num_list[i:i+windowsize]))
    return result

if __name__ == '__main__':
    print(max_kernel([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1],3))
    assert max_kernel([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
    num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
    k = 3
    print (max_kernel(num_list, k) )