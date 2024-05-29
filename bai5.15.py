import numpy as np

def f(x):
  if -1 <= x <= 1:
    return 0.5
  else:
    return 0

def P(n, eta, epsilon):
  # Tính xác suất của biến ngẫu nhiên S_n lớn hơn 3ηε
  integral = 0
  for x1 in np.arange(-1, 1, 0.01):
    for x2 in np.arange(-1, 1, 0.01):
      # ... (tính tích phân)
     return integral

# Ví dụ
n = 10
eta = 0.1
epsilon = 0.4

probability = P(n, eta, epsilon)
print(probability)
