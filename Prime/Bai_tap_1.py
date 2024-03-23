n = int(input())  # 5
if n < 2:
    print("No")
# Tạo ra 1 biến boolean True/False
kiem_tra_nto = True  ## Kiểm tra có phải nguyên tố hay không, mặc định là True
# Nhập n = 5
for i in range(2, n):
    if n % i == 0:
        kiem_tra_nto = False
        break
## Không in trong vòng lặp vì nếu in ra thì sẽ in ra nhiều lần
if kiem_tra_nto:
    print("Yes")
else:
    print("No")
# No - yes
