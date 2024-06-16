import math
import random


def loss_funtion(num_of_samples, loss_name):
    if (not num_of_samples.isnumeric()):
        print("number of samples must be an interger number")
    else:
        MAE = 0
        MSE = 0
        n = int(num_of_samples)
        for i in range(n):
            predict = random.uniform(0, 10)
            target = random.uniform(0, 10)
            if loss_name == "MAE":
                print(
                    f"loss_name: {loss_name},sample:{i},pred:{predict},target:{target},loss:{abs(predict - target)}")
            elif loss_name == "MSE":
                print(
                    f"loss_name: {loss_name},sample:{i},pred:{predict},target:{target},loss:{(predict - target)**2}")
            elif loss_name == "RMSE":
                print(
                    f"loss_name: {loss_name},sample:{i},pred:{predict},target:{target},loss:{math.sqrt((predict - target)**2)}")
            MAE += abs(predict - target)
            MSE += (predict - target)**2
        RMSE = math.sqrt(MSE)
        num_of_samples = int(num_of_samples)
        if loss_name == "MAE":
            print(f"final {loss_name}: {MAE/num_of_samples}")
        elif loss_name == "MSE":
            print(f"final {loss_name}: {MSE/num_of_samples}")
        elif loss_name == "RMSE":
            print(f"final {loss_name}: {RMSE/num_of_samples}")


if __name__ == "__main__":
    loss_funtion("8", 'MSE')
