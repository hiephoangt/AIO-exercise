import math


def sigmoid_funtion(x):
    return 1/(1 + math.exp(-x))


def relu_funtion(x):
    if x <= 0:
        return 0
    return x


def elu_funtion(x, alpha):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x)-1)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def activation_funtion(x, funtion):
    if (not is_number(x)):
        print("x must be a number")
    else:
        if (funtion not in ["sigmoid", "relu", "elu"]):
            print(f"{funtion} is not supported")
        else:
            float(x)
            if funtion == "sigmoid":
                print(f"sigmoid: f({x}) = {1/(1+ math.exp(-x))}")
            elif funtion == "relu":
                print(f"relu: f({x}) = {relu_funtion(x)}")
            else:
                print(f"ELU: f({x}) = {elu_funtion(x,0.01)}")


if __name__ == "__main__":
    activation_funtion(1.5, 'relu')
