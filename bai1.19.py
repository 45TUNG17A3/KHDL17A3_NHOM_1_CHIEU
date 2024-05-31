# Xác suất thị phần của mỗi cửa hàng
P_H_I = 2/5
P_H_II = 1/5
P_H_III = 2/5

# Tỉ lệ sản phẩm loại A trong mỗi cửa hàng
P_A_given_H_I = 0.70
P_A_given_H_II = 0.75
P_A_given_H_III = 0.50

# Tính tổng xác suất để khách hàng mua được sản phẩm loại A
P_A = P_H_I * P_A_given_H_I + P_H_II * P_A_given_H_II + P_H_III * P_A_given_H_III

# Sử dụng định lý Bayes để tính xác suất sản phẩm loại A được mua từ mỗi cửa hàng
P_H_I_given_A = (P_H_I * P_A_given_H_I) / P_A
P_H_II_given_A = (P_H_II * P_A_given_H_II) / P_A
P_H_III_given_A = (P_H_III * P_A_given_H_III) / P_A

# Kết quả
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng I: {P_H_I_given_A:.4f}")
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng II: {P_H_II_given_A:.4f}")
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng III: {P_H_III_given_A:.4f}")
# Xác suất thị phần của mỗi cửa hàng
P_H_I = 2/5
P_H_II = 1/5
P_H_III = 2/5

# Tỉ lệ sản phẩm loại A trong mỗi cửa hàng
P_A_given_H_I = 0.70
P_A_given_H_II = 0.75
P_A_given_H_III = 0.50

# Tính tổng xác suất để khách hàng mua được sản phẩm loại A
P_A = P_H_I * P_A_given_H_I + P_H_II * P_A_given_H_II + P_H_III * P_A_given_H_III

# Sử dụng định lý Bayes để tính xác suất sản phẩm loại A được mua từ mỗi cửa hàng
P_H_I_given_A = (P_H_I * P_A_given_H_I) / P_A
P_H_II_given_A = (P_H_II * P_A_given_H_II) / P_A
P_H_III_given_A = (P_H_III * P_A_given_H_III) / P_A

# Kết quả
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng I: {P_H_I_given_A:.4f}")
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng II: {P_H_II_given_A:.4f}")
print(f"Xác suất sản phẩm loại A được mua từ cửa hàng III: {P_H_III_given_A:.4f}")