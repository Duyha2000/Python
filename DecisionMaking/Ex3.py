character = input("Nhập vào một ký tự: ")

if character.isalpha():
    if character.isupper():
        print("upper-case alphabet")
    elif character.islower():
        print("lower-case alphabet")
else:
    print("not an alphabet")
