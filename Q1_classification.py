def evaluate_classification_model(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu của các giá trị đầu vào
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
    
    # Kiểm tra các giá trị đầu vào phải lớn hơn 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    
    # Tính Precision
    precision = tp / (tp + fp)
    
    # Tính Recall
    recall = tp / (tp + fn)
    
    # Tính F1-Score
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    # In kết quả
    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1 - score is {f1_score}')

# Ví dụ sử dụng hàm
evaluate_classification_model(2, 3, 4)
evaluate_classification_model('a', 3, 4)
evaluate_classification_model(2, 'a', 4)
evaluate_classification_model(2, 3, 'a')
evaluate_classification_model(2, 3, 0)
evaluate_classification_model(2.1, 3, 4)