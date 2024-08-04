import numpy as np

# Questions 1:


def compute_mean(X):
    return np.mean(X)


X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]

print(" Mean : ", compute_mean(X))

# Questions 2:


def compute_median(X):
    size = len(X)
    X = np . sort(X)
    print(X)
    if (size % 2 == 0):
        return 0.5*X[int(size/2)-1]+0.5*X[int(size/2)]
    else:
        return X[size/2-1]


X = [1, 5, 4, 4, 9, 13]
print(" Median : ", compute_median(X))

# Questions 3:


def compute_std(X):
    mean = compute_mean(X)
    variance = 0
    for i in X:
        variance += (i - mean)**2
    variance /= len(X)
    return np.sqrt(variance)


X = [171, 176, 155, 167, 169, 182]
print(compute_std(X))

# Questions 4:


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    xsum = 0
    ysum=0
    xysum = 0
    x2sum = 0
    y2sum = 0
    for i in range(N):
        xsum+=X[i]
        ysum+=Y[i]
        xysum+=X[i]*Y[i]
        x2sum += X[i]**2
        y2sum += Y[i]**2
    denominator = np.sqrt(N*x2sum - xsum**2)* np.sqrt(N*y2sum - ysum**2)
    numerator = N*xysum - xsum*ysum
    return np.round(numerator / denominator, 2)


X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print(" Correlation : ", compute_correlation_cofficient(X, Y))
