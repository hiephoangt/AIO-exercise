import numpy as np
import matplotlib.pyplot as plt


def get_column(data, index):
    result = [row[index] for row in data]
    return result


def prepare_data(file_name_dataset):
    data = np.genfromtxt(file_name_dataset, delimiter=',',
                         skip_header=1).tolist()

    # get tv (index=0)
    tv_data = get_column(data, 0)

    # get radio (index=1)
    radio_data = get_column(data, 1)

    # get newspaper (index=2)
    newspaper_data = get_column(data, 2)

    # get sales (index=3)
    sales_data = get_column(data, 3)

    # building X input  and y output for training
    # Create list of features for input
    X = [[1, x1, x2, x3]
         for x1, x2, x3 in zip(tv_data, radio_data, newspaper_data)]
    y = sales_data
    return X, y


def initialize_params():
    return [0, 0.016992259082509283, 0.0070783670518262355, -0.002307860847821344]


def predict(X_features, weights):
    return sum([X_features[i] * weights[i] for i in range(len(weights))])


def compute_loss(y_hat, y):
    return (y_hat - y) ** 2

# Compute gradient


def compute_gradient_w(X_features, y, y_hat):
    # Calculate the gradient for each weight
    dl_dweights = [2 * (y_hat - y) * X_features[i]
                   for i in range(len(X_features))]
    return dl_dweights

# Update weights


def update_weight(weights, dl_dweights, lr):
    # Update each weight
    updated_weights = [weights[i] - lr * dl_dweights[i]
                       for i in range(len(weights))]
    return updated_weights


def implement_linear_regression(X_feature, y_output, epoch_max=50, lr=1e-5):
    losses = []
    weights = initialize_params()
    N = len(y_output)
    for epoch in range(epoch_max):
        print("Epoch", epoch)
        for i in range(N):
            # Get a sample - row i
            features_i = X_feature[i]
            y = y_output[i]

            # Compute output
            y_hat = predict(features_i, weights)

            # Compute loss
            loss = compute_loss(y_hat, y)

            # Compute gradient w1, w2, w3, b
            dl_dweights = compute_gradient_w(features_i, y, y_hat)

            # Update parameters
            weights = update_weight(weights, dl_dweights, lr)

            # Logging
            losses.append(loss)
    return weights, losses


# Prepare data and run linear regression
X, y = prepare_data(
    "D:/Github/AIO-exercise/Module_4/Week1_LinearRegression/advertising.csv")
W, L = implement_linear_regression(X, y)

# Plot the losses
plt.plot(L[0:100])
plt.xlabel("#iteration")
plt.ylabel("Loss")
plt.title("Loss over first 100 iterations")
plt.show()

plt.plot(L[-100:])
plt.xlabel("#iteration")
plt.ylabel("MSE loss")
plt.title("MSE Loss over last 100 iterations")
plt.show()

# Multiple choices:
# Question 12:
W, L = implement_linear_regression(X, y)
# Print loss value at iteration 9999
print("Loss at iteration 9999:", L[9999] if len(
    L) > 9999 else "Not enough iterations")
