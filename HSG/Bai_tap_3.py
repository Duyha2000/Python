# Tạo một danh sách rỗng để lưu trữ số lần xuất hiện của mỗi chuỗi
counts = []

# Tạo một danh sách rỗng để lưu trữ chuỗi
strings = ["ABCD", "EFGH", "ABCD", "IJKL", "EFGH", "MNOP", "EFGH"]

# Tạo danh sách counts chứa số lần xuất hiện của mỗi chuỗi trong danh sách strings
for string in strings:
    counts.append(strings.count(string))

# Tìm chuỗi xuất hiện đúng một lần bằng cách duyệt qua từng phần tử của danh sách counts và strings
unique_string = None
for i in range(len(strings)):
    if counts[i] == 1:
        unique_string = strings[i]
        break

# In kết quả
if unique_string:
    print("Chuỗi xuất hiện đúng một lần là:", unique_string)
else:
    print("Không có chuỗi nào xuất hiện đúng một lần trong danh sách.")
