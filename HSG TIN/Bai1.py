# Tìm số lớn nhất trong 5 số nhập vào của người dùng

# Khởi tạo list rỗng để chứa 5 số nhập vào của người dùng và thêm vào list bằng hàm append của list (listNumber.append())
# và hàm int() để chuyển kiểu dữ liệu từ string sang int khi nhập vào từ bàn phím (int(input("Enter number: ")))
# và sử dụng hàm max() để tìm số lớn nhất trong list

listNumber = []
for i in range(5):
    listNumber.append(int(input("Enter number: ")))
print("Max number: ", max(listNumber))

# Nhập vào 5 số:
# Enter number: 3
# Enter number: 1
# Enter number: 5
# Enter number: 3
# Enter number: 5
# Max number:  5
