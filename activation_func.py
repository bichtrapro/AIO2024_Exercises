import math
def exercise2():
    x = input('Input x: ')
    if not is_number(x):
        print(f"{x} is not a number")
        return
    act_name = input('Enter activation function name:')
    #cast x to float
    result = cal_activation_func(x,act_name)

    if result is None:
        print(f"{act_name} is not supported")
    else:
        print(f"{act_name} + string(x) + string(result)")

def is_number(x):
    try:
        float(x) #type -casting the string to float
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
        raise ValueError("Hàm kích hoạt không hợp lệ. Chỉ hỗ trợ 'sigmoid', 'relu' và 'elu'.")

if __name__=="main":
    exercise2()
