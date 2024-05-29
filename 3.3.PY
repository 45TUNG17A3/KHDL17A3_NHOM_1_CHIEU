# Hàm tính giai thừa
def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Hàm tính tổ hợto_hop
def to_hop(n, k):
    return giai_thua(n) // (giai_thua(k) * giai_thua(n - k))

# Thông số
n = 9  # Tổng số lần lấy
k = 4  # Số lần nhận được bi vàng
p = 15 / 25  # Xác suất nhận được bi vàng trong mỗi lần lấy

# 1. Tính xác suất để có 4 lần nhận được bi vàng
xs_4lan_bi_vang = to_hop(n, k) * (p ** k) * ((1 - p) ** (n - k))
print("Xác suất để có 4 lần nhận được bi vàng:", xs_4lan_bi_vang)

# 2. Tính xác suất có điều kiện
xs_bi_vang = 4
kq = xs_4lan_bi_vang

# Xác suất P(B): Có 4 lần nhận được bi vàng
p_B = xs_4lan_bi_vang

# Xác suất P(A ∩ B): 4 lần nhận được bi vàng trong các lần lấy thứ chẵn
# Chọn 4 vị trí
