import math

# Bảng phân phối xác suất
X = [0.1, 0.4, 0.6]
P = [0.2, 0.3, 0.5]

# 1. Tính kỳ vọng E(X)
E_X = sum([X[i] * P[i] for i in range(len(X))])

# 2. Tính phương sai Var(X)
Var_X = sum([P[i] * (X[i] - E_X)**2 for i in range(len(X))])

# Độ lệch chuẩn (Standard Deviation)
std_dev_X = math.sqrt(Var_X)

# 3. Tính k cho Chebyshev
k = math.sqrt(0.4) / std_dev_X

# Sử dụng bất đẳng thức Chebyshev để đánh giá xác suất
chebyshev_prob = 1 - (1 / k**2)

print(f"Kỳ vọng E(X): {E_X:.4f}")
print(f"Phương sai Var(X): {Var_X:.4f}")
print(f"Độ lệch chuẩn std_dev_X: {std_dev_X:.4f}")
print(f"Xác suất của biến cố |X - E(X)| < sqrt(0.4): {chebyshev_prob:.4f}")