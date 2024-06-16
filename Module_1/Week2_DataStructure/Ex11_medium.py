def mediun(numlist):
    return sum(numlist)/len(numlist)

if __name__ == '__main__':
    assert mediun([4 , 6 , 8]) == 6
    print(mediun())