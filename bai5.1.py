# Hàm tính xác suất dựa vào bất đẳng thức Chebyshev
def bat_dang_thuc_chebyshev(n, p, k):
    # Kỳ vọng 
    ky_vong = n * p
    # Phương sai
    phuong_sai = n * p * (1 - p)
    # Xác suất P(|X - mu| >= k)
    xac_suat = phuong_sai / (k ** 2)
    return xac_suat

# Thông số bài toán
so_may = 10  # Số máy
xac_suat_hong = 0.05  # Xác suất máy hỏng

# a) Sai lệch nhỏ hơn 2
k1 = 2
xac_suat_sai_lech_nho_hon_2 = 1 - bat_dang_thuc_chebyshev(so_may, xac_suat_hong, k1)
print("Xác suất sai lệch nhỏ hơn 2:", xac_suat_sai_lech_nho_hon_2)

# b) Sai lệch lớn hơn 3
k2 = 3
xac_suat_sai_lech_lon_hon_3 = bat_dang_thuc_chebyshev(so_may, xac_suat_hong, k2)
print("Xác suất sai lệch lớn hơn 3:", xac_suat_sai_lech_lon_hon_3)