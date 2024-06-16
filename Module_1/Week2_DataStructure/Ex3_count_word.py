def count_word(filename):
    result = {}
    with open(filename,'r') as f:
        words = f.read()
        f.close()
        for word in words.split():
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result

if __name__ == '__main__':
    print(count_word('D:/Github/AIO-exercise/Module_1/Week2_DataStructure/P1_data.txt'))

    #Question 3:
    file_path = "D:/Github/AIO-exercise/Module_1/Week2_DataStructure/P1_data.txt"
    result = count_word (file_path)
    assert result ["who"] == 3
    print(result ["man"])