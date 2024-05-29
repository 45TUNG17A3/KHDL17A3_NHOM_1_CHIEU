P_cung_gioi_tinh = 0.64  
P_khac_gioi_tinh = 0.36

tong_xac_suat = 1
# P giả cùng giới tính = 0.5 * 0.5 + 0.5 * 0.5 = 0.5
# Hệ phương trình:
# P(T) + P(G) = 1
# P(T) + 0.5 * P(G) = 0.64

# Giải hệ phương trình
# P(T) + 0.5 * (1 - P(T)) = 0.64
# 0.5 * P(T) = 0.14
# P(T) = 0.28

P_T = 0.28
P_G = 1 - P_T

P_T_given_cung_gioi_tinh = P_T / P_cung_gioi_tinh

print("Tỉ lệ cặp sinh đôi thật là:", P_T)
print("Tỉ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính là:", P_T_given_cung_gioi_tinh)