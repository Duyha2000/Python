# Thực lĩnh =  ((lương chính * số ngày công) / 26) + (phụ cấp ) - (tạm ứng)
# 1 tháng làm việc 26 ngày, nghỉ quá 5 ngày sẽ bị trừ 20% thực lĩnh
# Làm thêm 3 ngày thì được 10% thực lĩnh
# Tính thực lĩnh của nhân viên
# Input: lương chính, số ngày công, phụ cấp, tạm ứng: 4 số nguyên

#########

# Nhập thông tin từ người dùng
luong_chinh = int(input("Nhập lương chính: "))
so_ngay_cong = int(input("Nhập số ngày công: "))
phu_cap = int(input("Nhập phụ cấp: "))
tam_ung = int(input("Nhập số tiền tạm ứng: "))

# Tính thực lĩnh ban đầu
thuc_linh = ((luong_chinh * so_ngay_cong) / 26) + phu_cap - tam_ung

# Xử lý trường hợp nghỉ quá 5 ngày
if so_ngay_cong < 21:
    thuc_linh *= 0.8

# Xử lý trường hợp làm thêm 3 ngày
if so_ngay_cong > 29:
    thuc_linh *= 1.1

# In kết quả
print("Thực lĩnh của nhân viên là:", thuc_linh)
