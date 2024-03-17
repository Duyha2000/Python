# # Nhập va 1 mảng số nguyên, tính tổng các phần tử trong mảng
# list = []
# n = int(input("Enter n: "))
# for i in range(n):
#     list.append(int(input("Enter number: ")))
# print("Sum of list: ", sum(list))
# # Tổng các số chia hết cho 3 trong mảng:
# sumDiv3 = 0
# for i in list:
#     if i % 3 == 0:
#         sumDiv3 += i
# print("Sum of number divisible by 3: ", sumDiv3)
luongchinh = int(input())
songaycong = int(input())
phucap = int(input())
tamung = int(input())
thuclinh = luongchinh * songaycong / 26 + phucap - tamung
# Nếu đi làm ít hơn 21 ngày, giảm 20% lương -> 80% lương
# Nếu nhận đầy đủ là 100% lương
if songaycong < 21:
    # thuclinh - 20 / 100
    thuclinh = thuclinh * 0.8
    # thuclinh *=0.8 (viết gọn)
if songaycong >= 29:
    # thuclinh + 10 / 100
    thuclinh = thuclinh * 1.1
    # thuclinh *=1.1 (viết gọn)
print(thuclinh)
