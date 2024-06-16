def check_the_number(n):
    list_of_number = []
    result = ""
    for i in range(1, 5):
        list_of_number.append(i)
    if n in list_of_number:
        result = "True"
    else:
        result = "False"
    return result


if __name__ == "__main__":
    N = 7
    assert check_the_number(N) == "False"

    N = 2
    results = check_the_number(N)
    print(results)
