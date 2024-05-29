import math

# Hàm tính tổ hợp C(n, k)
def combination(n, k):
    return math.comb(n, k)

# Tổng số cách chọn 6 người từ 10 người
so_cach_chon = combination(10, 6)

# 1) Xác suất để cả 6 người là nam
chon_6_nam = combination(6, 6)
xac_suat_1 = chon_6_nam / so_cach_chon

# 2) Xác suất để có 4 nam và 2 nữ
chon_4nam_va_2nu = combination(6, 4) * combination(4, 2)
xac_suat_2 = chon_4nam_va_2nu / so_cach_chon

# 3) Xác suất để có ít nhất 2 nữ
# Các trường hợp: 2 nữ và 4 nam, 3 nữ và 3 nam, 4 nữ và 2 nam
chon_2nu_4nam = combination(6, 4) * combination(4, 2)
chon_3nu_3nam = combination(6, 3) * combination(4, 3)
chon_4nu_2nam = combination(6, 2) * combination(4, 4)

truong_hop_co_it_nhat_2nu = (chon_2nu_4nam + chon_3nu_3nam + chon_4nu_2nam)
xac_suat_3 = truong_hop_co_it_nhat_2nu / so_cach_chon

# Kết quả
print(f"Xác suất để cả 6 người là nam: {xac_suat_1:.5f}")
print(f"Xác suất để có 4 nam và 2 nữ: {chon_4nam_va_2nu:.5f}")
print(f"Xác suất để có ít nhất 2 nữ: {xac_suat_3:.5f}")
