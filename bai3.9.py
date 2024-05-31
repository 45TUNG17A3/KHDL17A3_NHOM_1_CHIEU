import scipy.stats as stats

# Tham số của phân phối nhị thức
n = 650
p = 0.7

# 1) Tính xác suất để số sinh viên đến đọc sách tại thư viện trong ngày ít hơn 440 sinh viên
# Sử dụng xấp xỉ phân phối chuẩn
mean = n * p
std = (n * p * (1 - p)) ** 0.5

# Tính xác suất P(X < 440)
z_score = (440 - mean) / std
probability_less_than_440 = stats.norm.cdf(z_score)

print(f'Xác suất để số sinh viên đến đọc sách tại thư viện trong ngày ít hơn 440 sinh viên: {probability_less_than_440:.4f}')

# 2) Tính số ghế cần chuẩn bị với xác suất 0,99 đảm bảo đủ chỗ cho sinh viên
# Tìm k sao cho P(X <= k) >= 0.99
prob_needed = 0.99
z_needed = stats.norm.ppf(prob_needed)

# Tìm số ghế cần thiết
k_needed = mean + z_needed * std

print(f'Số ghế cần chuẩn bị để với xác suất 0,99 có thể đảm bảo đủ ghế chỗ cho sinh viên đến đọc sách: {int(k_needed) + 1}')