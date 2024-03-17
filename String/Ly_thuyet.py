ls = [1, 2, 3, 4]
# Theo chiều từ trái sang phải (từ đầu đến cuối) thì index của mảng là 0, 1, 2, 3
# Theo chiều từ phải sang trái (từ cuối đến đầu) thì index của mảng là -1, -2, -3, -4
print(ls[0])
print(ls[-1])
# Đếm số phần tử trong mảng: len(mảng)
print(len(ls))  # 4
print(sum(ls))  # 10

# In ra các số trong mảng
for i in ls:
    print(i, end=" ")
print()
string = "Hello"
print(string[0])  # H
print(string[4])  # o
print(string[-2])  # l
# In ra các ký tự trong chuỗi
for i in string:
    print(i, end=" ")
print()
# Cắt chuỗi: chuỗi[begin:end:step]
str = "Xin chao cac ban!"
# khoảng trắng là 1 ký tự
print(str[0:6])  # Xin ch
print(str[4:12])  # chao cac
print(str[-6: -1])  # c ban (giữ nguyên -6, -1 phải trừ -1 đơn vị nữa là -2)
print(str[-4: -2])  # ba (giữ nguyên -6, -2 phải trừ -1 đơn vị nữa là -3)
print(str[-9:-4])  # cac
# [ bắt đầu : kết thúc : bước nhảy ]
# lấy đầu bỏ đuôi
# giá trị bắt đầu đi từ trái sang phải
print(str[2:])  # n chao cac ban!
print(str[5:])  # hao cac ban!
print(str[-4:])  # ban! (lấy từ -4 đến hết)
print(str[-7:])  # ac ban! (lấy từ -7 đến hết)
# Giá trị kết thúc:
print(str[:5])  # Xin c
print(str[:9])  # Xin chao
# Bước nhảy:
str2 = "Xin chao cac ban!"
print(str2[0:5:2])  # 0 2 4 - x n c
print(str2[2:9:3])  # 2 5 8
print(str2[1:6:2])  # 1 3 5 - i h
# Replace: thay thế chuỗi con trong chuỗi bằng chuỗi khác:
str3 = str2.replace("Xin chao", "Tam biet")
print(str3)  # Tam biet cac ban!
