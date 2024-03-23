# Bước 1: Nhập số n
n = int(input("Nhập số nguyên dương n: "))
lst = set()  # Sử dụng một tập hợp để lưu trữ các phần tử khác nhau


# Bước 2: Viết hàm tính số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Bước 3: Tìm và tính số nguyên tố rút gọn của n
for i in range(2, n):
    if isPrime(i) and n % i == 0:
        lst.add(i)  # Thêm phần tử vào tập hợp

# Bước 4: In ra tổng các thừa số nguyên tố của n
print("Tổng các thừa số nguyên tố của n là:", sum(lst))

# Bước 5: In ra các số có cùng số nguyên tố rút gọn với n trong đoạn a đến b
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
print(f"Các số có cùng số nguyên tố rút gọn với {n} trong đoạn từ {a} đến {b} là:")
for num in range(a, b + 1):
    prime_factors_num = set()
    for i in range(2, num):
        if isPrime(i) and num % i == 0:
            prime_factors_num.add(i)
    if sum(prime_factors_num) == sum(lst):
        print(num)
