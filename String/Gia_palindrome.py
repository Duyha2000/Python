# Chuỗi giả palindrome: abc123cba
# Nhập vào một chuỗi, kiểm tra xem chuỗi đó có phải là chuỗi giả palindrome không
# Nhập n = 3 -> abc123cba là chuỗi giả palindrome với n = 3:

# abcd123bad không phải là chuôỗi giả palindrome với n = 3:
# abc đảo ngược lại là cba, 3 ký tự cuối là bad

# abc123cba
s = input()
n = int(input())
if s[0:n: 1] == s[-1:-n - 1:-1]:
    print("Y")
else:
    print("N")
