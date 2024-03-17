# Chuỗi Palindrome
# Bài tập:
# Chuỗi Palindrome là các chuỗi có dạng khi viết xuôi và viết ngược thì nó đều có dạng như nhau.
# Chẳng hạn: aba, acca, iiiuuuiii,... là các chuỗi có dạng Palindrome.
# Hãy viết chương trình kiểm tra xem một chuỗi được nhập vào từ bàn phím có phải là một chuỗi Palindrome hay không?
# Nếu có hãy in ra màn hình:
# Chuỗi vừa nhập là chuỗi Palindrome!
# Ngược lại, khi chuỗi nhập vào không phải là chuỗi Palindrome thì in ra màn hình:
# Chuỗi vừa nhập KHÔNG phải là một chuỗi Palindrome!
s = input()
if s == s[::-1]:
    print("Chuỗi vừa nhập là chuỗi Palindrome!")
else:
    print("Chuỗi vừa nhập KHÔNG phải là một chuỗi Palindrome!")
