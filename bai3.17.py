import math

# Hàm tính CDF của phân phối chuẩn
def normal_cdf(x, mu, sigma):
    return (1 + math.erf((x - mu) / (sigma * math.sqrt(2)))) / 2

# Hàm tính giá trị nghịch đảo của erf
def inverse_erf(x):
    a = 0.147
    sign = 1 if x >= 0 else -1
    ln = math.log(1 - x**2)
    return sign * math.sqrt(math.sqrt((2/(math.pi*a) + ln/2)**2 - ln/a) - (2/(math.pi*a) + ln/2))

# Tỷ lệ chỗ đậu xe có thể sử dụng
mu = 4  # Giá trị trung bình
sigma = 0.1 * mu  # Độ lệch chuẩn
x = 1.15 * mu  # Chiều dài của xe hơi cao cấp
z = (x - mu) / sigma  # Giá trị Z tương ứng

# Tính xác suất P(X >= 1.15 * mu)
p_x_ge_1_15_mu = 1 - normal_cdf(x, mu, sigma)
print("Tỷ lệ chỗ đậu xe có thể sử dụng:", p_x_ge_1_15_mu)

# Chiều dài của xe để sử dụng 90% chỗ đậu xe
# P(X >= L) = 0.10 nghĩa là P(X < L) = 0.90
p = 0.90
z_90 = math.sqrt(2) * inverse_erf(2 * p - 1)  # Tính z từ P(Z < z) = 0.90
L = mu + z_90 * sigma  # Chiều dài L tương ứng

print("Chiều dài của xe để sử dụng 90% chỗ đậu xe là:", L)