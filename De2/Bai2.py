def xoa_khoang_trang_thua(s):
    # Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
    s = s.strip()
    # Su dung vong lap while de lap cho toi khi het khoang trang thua
    while "  " in s:
        # Su dung phuong thuc replace() de thay the 2 khoang trang thanh 1 khoang trang
        s = s.replace("  ", " ")
    return s


def viet_hoa_chuCai_dau_cau(s):
    # Tach cac cau trong chuoi
    cau = s.split('. ')
    # Duyet qua tung cau va viet hoa chu cai dau tien cua cau do
    for i in range(len(cau)):
        cau[i] = cau[i].capitalize()
    # Ghep lai cac cau voi dau cham phia truoc
    s = '. '.join(cau)
    return s


# Nhap gia tri tu ban phim
s = input()

# Xoa khoang trang thua va viet hoa chu cai dau cua moi cau
result = viet_hoa_chuCai_dau_cau(xoa_khoang_trang_thua(s))

# In chuoi ket qua
print(result)
