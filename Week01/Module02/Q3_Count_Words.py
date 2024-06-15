import gdown

url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'P1_data.txt'

# Tải file
gdown.download(url, output, quiet=False)

def word_count(file_path):
    word_count_dict = {}
    
    # Đọc nội dung từ file
    with open(file_path, 'r') as file:
        for line in file:
            # Tách dòng thành các từ và chuyển thành chữ thường
            words = line.strip().lower().split()
            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

    sorted_word_count = dict(sorted(word_count_dict.items()))
    return sorted_word_count

file_path = 'P1_data.txt'
print(word_count(file_path))