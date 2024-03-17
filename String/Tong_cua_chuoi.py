# Đầu vào: Nhập vào một chuỗi, tính tổng các chữ số trong chuỗi
s = input()  # "123abc456"
# Đầu ra: 1 + 2 + 3 + 4 +5 +6 = 21
# B1: Dùng vòng lặp for để lấy ra các ký tự trong chuỗi đó:
# thu được 1 2 3 a b c 4 5 6
# B2: Kiểm tra xem ký tự đó có phải là số không:isdigit()
# B3: Nếu là số thì chuyển nó về kiểu số int() và cộng dồn lại
tong = 0  # Khởi tạo biến tổng
for i in s:
    if i.isdigit():
        tong += int(i)

print(tong)
