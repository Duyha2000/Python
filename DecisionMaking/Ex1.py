## Tìm số lớn nhất trong 3 số
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Max is", max)
