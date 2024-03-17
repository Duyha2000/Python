n = int(input())  # n là số phần tử trong mảng
li = []  # Khởi tạo 1 danh sách / mảng -> sau đấy đẩy các số vào mảng bằng append
# Đẩy các số vào trong mảng
for i in range(n):
    li.append(int(input()))
print(li)


# 13: 1 13 : chia heest cho 1 và chính nó: 2 - 12
def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# In ra các số nguyên tố trong mảng
for i in li:
    if isprime(i):
        print(i, end=" ")
