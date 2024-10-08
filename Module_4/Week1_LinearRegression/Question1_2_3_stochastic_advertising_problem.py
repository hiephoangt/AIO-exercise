# Bai 1
# dataset
import numpy as np
import matplotlib.pyplot as plt
import random


def get_column(data, index):
    result = [row[index] for row in data]
    return result


def prepare_data(file_name_dataset):
    data = np.genfromtxt(file_name_dataset, delimiter=',',
                         skip_header=1).tolist()
    N = len(data)

    # get tv (index = 0)
    tv_data = get_column(data, 0)

    # get radio (index = 1)
    radio_data = get_column(data, 1)

    # get newspaper (index = 2)
    newspaper_data = get_column(data, 2)

    # get sales (index = 3)
    sales_data = get_column(data, 3)

    # building X input and y output for training
    X = [tv_data, radio_data, newspaper_data]
    y = sales_data
    return X, y


X, y = prepare_data(
    "D:/Github/AIO-exercise/Module_4/Week1_LinearRegression/advertising.csv")
lst = [sum(X[0][:5]), sum(X[1][:5]), sum(X[2][:5]), sum(y[:5])]
print(lst)

#Bai 2
def initialize_params():
    w1, w2, w3, b = (0.016992259082509283,
                     0.0070783670518262355, -0.002307860847821344, 0)
    return w1, w2, w3, b


def implement_linear_regression(X_data, y_data, epoch_max=50, lr=1e-5):
    losses = []
    w1, w2, w3, b = initialize_params()

    N = len(y_data)
    for epoch in range(epoch_max):
        for i in range(N):
            #get a sample 
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]

            y = y_data[i]

            #compute output
            y_hat = predict(x1,x2,x3,w1,w2,w3,b)

            #compute loss
            loss = compute_loss_mse(y, y_hat)

            #compute gradient w1,w2,w3,b
            dl_dw1 = compute_gradient_wi(x1,y,y_hat)
            dl_dw2 = compute_gradient_wi(x2,y,y_hat)
            dl_dw3 = compute_gradient_wi(x3,y,y_hat)

            dl_db = compute_gradient_b(y,y_hat)

            #update params
            w1 = update_weight_wi(w1,dl_dw1,lr)
            w2 = update_weight_wi(w2,dl_dw2,lr)
            w3 = update_weight_wi(w3,dl_dw3,lr)
            b = update_weight_b(b,dl_db,lr)

            #logging 
            losses.append(loss)
    return (w1,w2,w3,b,losses)
            
def predict(x1,x2,x3,w1,w2,w3,b):
    return x1*w1+x2*w2+x3*w3+b
def compute_loss_mse(y, y_hat):
    return (y - y_hat)**2
def compute_gradient_wi(xi,y,y_hat):
    return  2 *xi*(y_hat-y)
def compute_gradient_b(y,y_hat):
    return 2 * (y_hat - y)
def update_weight_wi(wi,dl_dwi,lr):
    return wi - lr * dl_dwi
def update_weight_b(b,dl_db,lr):
    return b - lr * dl_db

# Question 2
print(predict(1,1,1,0,0.5,0,0.5))

# Question 3
l =compute_loss_mse(y_hat=1,y=0.5)
print(l)

# Question 4
g_wi = compute_gradient_wi(xi=1.0,y=1.0,y_hat=0.5)
print(g_wi)

# Question 5 
g_b = compute_gradient_b(y=2.0, y_hat=0.5)
print(g_b)

# Question 6
after_wi = update_weight_wi(wi=1.0,dl_dwi=-0.5,lr=1e-5)
print(after_wi)

# Question 7 
after_b = update_weight_b(b=0.5,dl_db=-1.0, lr=1e-5)
print(after_b)
print(after_wi)

(w1,w2,w3,b,losses) = implement_linear_regression(X,y)
plt.plot(losses[:100])
plt.xlabel("#iteration")
plt.ylabel("Loss")
plt.show()

# Question 8
print(w1,w2,w3)

# Question 9
tv = 19.2
radio = 35.9
newspaper = 51.3

sales = predict(tv,radio,newspaper,w1,w2,w3,b)
print(f"predicted sales is {sales}")

# Question 10
def compute_loss_mae(y,y_hat):
    return abs(y-y_hat)
l = compute_loss_mae(y=0.5,y_hat=1)
print(l)

#Bai 3
def implement_linear_regression_nsamples(X_data,y_data,epoch_max = 1000,lr = 1e-5):
    losses = []

    w1,w2,w3,b =initialize_params()
    N = len(y_data)

    for _ in range(epoch_max):
        loss_total = 0
        dw1_total = 0
        dw2_total = 0
        dw3_total = 0
        db_total = 0

        for i in range(N):
            #get a sample 
            x1 = X_data[0][i]
            x2 = X_data[1][i]
            x3 = X_data[2][i]

            y = y_data[i]

            #compute output
            y_hat = predict(x1,x2,x3,w1,w2,w3,b)

            #compute loss
            loss = compute_loss_mse(y, y_hat)

            loss_total+=loss

            #compute gradient w1,w2,w3,b
            dl_dw1 = compute_gradient_wi(x1,y,y_hat)
            dl_dw2 = compute_gradient_wi(x2,y,y_hat)
            dl_dw3 = compute_gradient_wi(x3,y,y_hat)

            dl_db = compute_gradient_b(y,y_hat)

            dw1_total+=dl_dw1
            dw2_total+=dl_dw2
            dw3_total+=dl_dw3
            db_total+=dl_db
        
        #update params
        w1 = update_weight_wi(w1,dw1_total/N,lr)
        w2 = update_weight_wi(w2,dw2_total/N,lr)
        w3 = update_weight_wi(w3,dw3_total/N,lr)
        b = update_weight_b(b,db_total/N,lr)
        
        #logging
        losses.append(loss_total/N)
    return (w1,w2,w3,b,losses)

(w1,w2,w3,b,losses) = implement_linear_regression_nsamples(X,y)
plt.plot(losses)
plt.xlabel("#iteration")
plt.ylabel("MSE Loss")
plt.show()
print(w1,w2,w3,b)