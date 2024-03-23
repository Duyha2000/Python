n = list(map(int, input().split()))
dem = 0


def nguyento(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


for i in n:
    if nguyento(i):
        print(i)
        dem += 1
print(dem)
