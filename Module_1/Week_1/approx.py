def giai_thua(n):
    if n == 0:
        return 1
    return n*giai_thua(n-1)


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i+1))/giai_thua(2*i+1)
    return result


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i)*(x**(2*i))/giai_thua(2*i)
    return result


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i+1))/giai_thua(2*i+1)
    return result


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i))/giai_thua(2*i)
    return result


if __name__ == '__main__':
    print(round(approx_sin(3.14, 10), 4))
    print(round(approx_cos(3.14, 10), 2))
    print(round(approx_sinh(3.14, 10), 2))
    print(round(approx_cosh(1, 10), 2))
