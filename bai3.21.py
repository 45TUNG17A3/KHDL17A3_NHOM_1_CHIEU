import numpy as np
from scipy.integrate import quad

# Tham số của phân phối mũ
lambda_param = 2

# 1. Tính kỳ vọng của Y = e^(-X)
def integrand_expectation(x):
    return np.exp(-x) * lambda_param * np.exp(-lambda_param * x)

expectation_Y, _ = quad(integrand_expectation, 0, np.inf)

print(f'Kỳ vọng của Y = e^(-X): {expectation_Y:.4f}')

# 2. Tính E(Y^2)
def integrand_second_moment(x):
    return (np.exp(-x))**2 * lambda_param * np.exp(-lambda_param * x)

second_moment_Y, _ = quad(integrand_second_moment, 0, np.inf)

# 3. Tính độ lệch chuẩn của Y
variance_Y = second_moment_Y - expectation_Y**2
std_dev_Y = np.sqrt(variance_Y)

print(f'Độ lệch chuẩn của Y = e^(-X): {std_dev_Y:.4f}')