def character_count(word):
    dic = {}
    for i in word:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


if __name__ == '__main__':
    print(character_count("Happinessh"))

    # Question 2:
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))
