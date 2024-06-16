def reverse_string(s):
    result = ""
    for i in range(len(s)):
        result += s[len(s) - i - 1]
    return result

if __name__ == '__main__':

    x = 'I can do it'
    assert reverse_string(x) =='ti od nac I'

    x = 'apricot'
    print(reverse_string(x))