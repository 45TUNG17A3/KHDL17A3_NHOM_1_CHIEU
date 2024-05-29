def tinh_toan():
    # Xác suất các khẩu pháo trúng mục tiêu
    p_A1 = 0.4
    p_A2 = 0.7
    p_A3 = 0.8
    
    # Xác suất mục tiêu bị tiêu diệt khi trúng 1, 2, 3 phát đạn
    p_D1 = p_A1 * (1 - p_A2) * (1 - p_A3) + (1 - p_A1) * p_A2 * (1 - p_A3) + (1 - p_A1) * (1 - p_A2) * p_A3
    p_D2 = p_A1 * p_A2 * (1 - p_A3) + p_A1 * (1 - p_A2) * p_A3 + (1 - p_A1) * p_A2 * p_A3
    p_D3 = p_A1 * p_A2 * p_A3
    
    # Xác suất mục tiêu bị tiêu diệt
    p_D = p_D1 * 0.3 + p_D2 * 0.7 + p_D3 * 1
    
    # Xác suất để cả 3 khẩu pháo đóng góp vào việc tiêu diệt mục tiêu
    p_A1_A2_A3_given_D = p_D3 / p_D
    
    return p_D, p_A1_A2_A3_given_D

p_D, p_A1_A2_A3_given_D = tinh_toan()

print("Xác suất để mục tiêu bị tiêu diệt:", p_D)
print("Xác suất để cả 3 khẩu pháo đóng góp vào việc tiêu diệt mục tiêu:", p_A1_A2_A3_given_D)