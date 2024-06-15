import math
import random
def is_number(x):
    try:
        int(x) # Chuyển đổi kiểu từ string sang int
    except ValueError:
        return False
    return True

#mae function
def mae(y_true,y_pred,num_samples):
    total_loss = 0
    for i in range(len(y_true)):
        total_loss += abs(y_true[i]- y_pred[i])
    return total_loss/num_samples

#mse function
def mse(y_true,y_pred,num_samples):
    total_loss = 0
    for i in range(len(y_true)):
        total_loss += (y_true[i]- y_pred[i])**2
    return total_loss/num_samples

#rmse function
def rmse(y_true,y_pred,num_samples):
    return math.sqrt(mse(y_true,y_pred,num_samples))




def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not is_number(num_samples):
        print(f"{num_samples} is not a number")
        return
    
    # Chuyển đổi x sang kiểu int
    num_samples = int(num_samples)
    predictions = [random.uniform(0,10) for _ in range(num_samples)]
    targets = [random.uniform(0,10) for _ in range(num_samples)]
    # Nhap vao loss name
    loss_name = input('Input loss name:')
    if loss_name == 'MAE':
        loss = mae(targets, predictions,num_samples)
    elif loss_name == 'MSE':
        loss = mse(targets,predictions,num_samples)
    elif loss_name == 'RMSE':
        loss = rmse(targets,predictions,num_samples)
    else:
        print(f"{loss_name} is not supported")
        return

    print(f"loss name: {loss_name}")
    for i in range(num_samples):
        print(f"sample {i}: predict = {predictions[i]}, target = {targets[i]}")
    print(f"loss: {loss}")
    
if __name__ == "__main__":
    exercise3()