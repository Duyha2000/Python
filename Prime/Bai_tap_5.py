def findGCD(a, b):
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            GCD = i
    return GCD


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
GCD = findGCD(a, b)  ## 12
print("GCD:", GCD)
