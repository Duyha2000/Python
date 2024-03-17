# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Mảng dữ liệu
array = list(map(int, input().split()))  # 3 , 4 , 2 , 5 , 7
# Sắp xếp mảng tăng dần
array.sort()  # 2 3 4 5 7
# In ra mảng sau khi sắp xếp
print("Mảng sau khi sắp xếp tăng dần là:", array)

# Tính tổng của các phần tử trong mảng
array_sum = sum(array)

# Tìm các phần tử không trùng nhau trong mảng
array_set = set(array)

# Tính tổng của các số nguyên tố trong mảng
prime_sum = 0
for num in array_set:
    if is_prime(num):
        prime_sum += num

# Đếm số lượng số nguyên tố trong mảng
count = 0
for num in array_set:
    if is_prime(num):
        count += 1

# In ra số lượng số nguyên tố
print("Số lượng số nguyên tố trong mảng là:", count)

# Hiển thị các số nguyên tố
print("Các số nguyên tố khác nhau trong mảng là:")

for num in array_set:
    if is_prime(num):
        print(num, end=" ")

print()
# In ra tổng các số nguyên tố
print("Tổng các số nguyên tố trong mảng là:", prime_sum)

# Tìm số nguyên k sao cho 2^k lớn hơn tổng các phần tử trong mảng
k = 0
for k in range(array_sum):
    if pow(2, k) > array_sum:
        break

# In ra số nguyên k nhỏ nhất thỏa mãn điều kiện
print("Số nguyên k nhỏ nhất thỏa mãn đkien 2^k > array_sum là:", k)
