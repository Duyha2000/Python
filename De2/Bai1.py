# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Mảng dữ liệu
array = [6, 7, 3, 3, 4, 2]

# Tính tổng của các phần tử trong mảng
array_sum = sum(array)

# Tìm số nguyên k sao cho 2^k lớn hơn tổng các phần tử trong mảng
for k in range(array_sum):
    if 2 ** k > array_sum:
        break

# In ra số nguyên k nhỏ nhất thỏa mãn điều kiện
print("Số nguyên k nhỏ nhất là:", k)

# Tính tổng của các số nguyên tố trong mảng
prime_sum = 0
for num in array:
    if is_prime(num):
        prime_sum += num

# In ra tổng các số nguyên tố
print("Tổng các số nguyên tố trong mảng là:", prime_sum)
