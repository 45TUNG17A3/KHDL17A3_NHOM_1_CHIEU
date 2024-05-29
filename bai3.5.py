import math

# Hàm tính hệ số nhị thức
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Hàm tính xác suất nhị thức
def binomial_probability(n, k, p):
    binom_coeff = binomial_coefficient(n, k)
    probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
    return probability

# Các tham số cho phân phối nhị thức kết hợp
n = 30
p = 0.1
k = 4

# Tính xác suất
probability = binomial_probability(n, k, p)

print(f"P(X + Y + Z = 4) = {probability:.8f}")