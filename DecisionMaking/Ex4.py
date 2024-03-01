import math

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
delta = b ** 2 - 4 * a * c
if a == 0:
    x = -c / b
    print(f"One solution {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Two solutions {x1} and {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"One solution {x}")
    else:
        print("No solution")
