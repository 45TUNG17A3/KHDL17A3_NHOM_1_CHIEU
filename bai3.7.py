p_gai = 0.52  # Xác suất sinh bé gái
p_trai = 1 - p_gai  # Xác suất sinh bé trai
print("Xác suất sinh được một bé trai là:", p_trai)

def to_hop(tong_so_lan_thu, k):
    if k > tong_so_lan_thu - k:
        k = tong_so_lan_thu - k
    ket_qua = 1
    for i in range(k):
        ket_qua = ket_qua * (tong_so_lan_thu - i) // (i + 1)
    return ket_qua

def xac_suat_nhi_thuc(tong_so_lan_thu, k, p):
    to_hop_ck = to_hop(tong_so_lan_thu, k)
    xac_suat = to_hop_ck * (p ** k) * ((1 - p) ** (tong_so_lan_thu - k))
    return xac_suat

tong_so_lan_thu = 300

k1 = 180
xac_suat_180_trai = xac_suat_nhi_thuc(tong_so_lan_thu, k1, p_trai)
print(f"Xác suất có 180 bé trai: {xac_suat_180_trai:.10f}")

xac_suat_150_den_170_trai = sum(xac_suat_nhi_thuc(tong_so_lan_thu, k, p_trai) for k in range(150, 171))
print(f"Xác suất số bé trai sinh ra từ 150 đến 170: {xac_suat_150_den_170_trai:.10f}")

xac_suat_it_hon_170_trai = sum(xac_suat_nhi_thuc(tong_so_lan_thu, k, p_trai) for k in range(170))
print(f"Xác suất số bé trai sinh ra ít hơn 170: {xac_suat_it_hon_170_trai:.10f}")