def probability_red_ball():
    # Xác suất rút mỗi loại bóng từ hộp đầu tiên
    P_R1 = 5 / 20
    P_W1 = 15 / 20
    
    # Xác suất có điều kiện rút mỗi loại bóng từ hộp thứ hai sau khi chuyển một quả bóng đỏ
    P_R2_given_R1 = 7 / 16
    P_W2_given_R1 = 9 / 16
    
    # Xác suất có điều kiện rút mỗi loại bóng từ hộp thứ hai sau khi chuyển một quả bóng trắng
    P_R2_given_W1 = 6 / 16
    P_W2_given_W1 = 10 / 16
    
    # Xác suất tổng cộng rút một quả bóng đỏ từ hộp thứ hai
    P_R2 = P_R2_given_R1 * P_R1 + P_R2_given_W1 * P_W1
    
    # Xác suất tổng cộng rút một quả bóng trắng từ hộp thứ hai
    P_W2 = P_W2_given_R1 * P_R1 + P_W2_given_W1 * P_W1
    
    return P_R2, P_W2

P_R2, P_W2 = probability_red_ball()

print(f"Xác suất rút một quả bóng đỏ: {P_R2}")
print(f"Xác suất rút một quả bóng trắng: {P_W2}")
