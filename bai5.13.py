import random

def sinh_bien_ngau_nhien(k, s):
    return k * s if random.random() < 0.5 else -k * s

def luat_so_lon_cua_chebyshev(n, k, s):
    tong_x = 0
    for i in range(1, n + 1):
        x_i = sinh_bien_ngau_nhien(k, s)
        tong_x += x_i
        trung_binh_x = tong_x / i
        print(f"Mẫu {i}: X_{i} = {x_i}, Trung bình = {trung_binh_x}")

# Tham số
n = 1000  # Số lượng mẫu
k = 1     # Giá trị của k
s = 2     # Giá trị của s

luat_so_lon_cua_chebyshev(n, k, s)