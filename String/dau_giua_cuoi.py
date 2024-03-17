s1 = input()
s2 = input()

# Lấy ký tự đầu:
s3 = s1[0]
s4 = s2[0]

# Lấy ký tự giữa
s5 = s1[len(s1) // 2]  # // là phép chia lấy phần nguyên
s6 = s2[len(s2) // 2]

# Lấy ký tự cuối
s7 = s1[-1]
s8 = s2[-1]

# Gộp vào một ký tự:
s = s3 + s4 + s5 + s6 + s7 + s8
print(s)
