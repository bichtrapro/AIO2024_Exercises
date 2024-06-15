def sliding_window_maximum(lst, k):
    n = len(lst)
    if n * k == 0:
        return []

    result = []
    for i in range(n - k + 1):
        window_max = max(lst[i:i + k])
        result.append(window_max)

    return result

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
print(sliding_window_maximum(num_list, k))