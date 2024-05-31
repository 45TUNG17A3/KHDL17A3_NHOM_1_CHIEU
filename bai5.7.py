import numpy as np

# Xác suất để một chi tiết sản xuất ra đạt tiêu chuẩn
p = 0.8

# Số lượng sản phẩm
n = 4000

# Giới hạn dưới và trên
lower_bound = 0.78 * n
upper_bound = 0.83 * n

# Trung bình mong đợi
mu = p

# Phương sai
sigma_squared = p * (1 - p)

# Giá trị k
k = (upper_bound - lower_bound) / 2

# Tính xác suất
probability = 1 - 1 / k**2

print("Xác suất tỷ lệ chi tiết đạt tiêu chuẩn nằm trong khoảng từ 78% đến 83% là:", probability)