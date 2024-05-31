# Xác định không gian mẫu
khong_gian_mau = [(a, b) for a in range(1, 7) for b in range(1, 7)]

# Xác định biến cố tổng số chấm bằng 7
bien_co_tong_7 = [(a, b) for a, b in khong_gian_mau if a + b == 7]

# Tính xác suất
xac_suat_tong_7 = len(bien_co_tong_7) / len(khong_gian_mau)

# Kết quả
print(f"Không gian mẫu: {khong_gian_mau}")
print(f"Các cặp có tổng số chấm bằng 7: {bien_co_tong_7}")
print(f"Xác suất để tổng số chấm bằng 7: {xac_suat_tong_7}")