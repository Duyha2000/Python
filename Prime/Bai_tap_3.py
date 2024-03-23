def nguyento(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


i = 2
count = 0
while count < 20:
    if nguyento(i):
        count += 1
        print(i)
    i += 1
