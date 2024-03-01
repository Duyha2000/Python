month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month == 2:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("29 days")
            else:
                print("28 days")
        else:
            print("29 days")
    else:
        print("28 days")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
else:
    print("Invalid month")
