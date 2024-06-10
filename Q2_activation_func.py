import math

def exercise2():
    x = input('Input x: ')
    if not is_number(x):
        print(f"{x} is not a number")
        return
    act_name = input('Enter activation function name:')
    
    # Chuyển đổi x sang kiểu float
    x = float(x)
    result = cal_activation_func(x, act_name)

    if result is None:
        print(f"{act_name} is not supported")
    else:
        print(f"{act_name}({x}) = {result}")

def is_number(x):
    try:
        float(x) # Chuyển đổi kiểu từ string sang float
    except ValueError:
        return False
    return True

def cal_activation_func(x, act_name):
    if act_name == 'sigmoid':
        return 1 / (1 + math.exp(-x))
    elif act_name == 'relu':
        return max(0, x)
    elif act_name == 'elu':
        alpha = 0.01  
        if x >= 0:
            return x
        else:
            return alpha * (math.exp(x) - 1)
    else:
        return None

if __name__ == "__main__":
    exercise2()
