# Nhập va 1 mảng số nguyên, tính tổng các phần tử trong mảng
list = []
n = int(input("Enter n: "))
for i in range(n):
    list.append(int(input("Enter number: ")))
print("Sum of list: ", sum(list))
# Tổng các số chia hết cho 3 trong mảng:
sumDiv3 = 0
for i in list:
    if i % 3 == 0:
        sumDiv3 += i
print("Sum of number divisible by 3: ", sumDiv3)
