Pa = 0.7 # Xác suất người mua mua hộp số tự động
Pb = 0.75 # Xác suất người mua mua động cơ V6
Pc = 0.8 # Xác suất người mua mua điều hòa nhiệt độ
Pa_u_b = 0.8
Pa_u_c = 0.85
Pb_u_c = 0.9
Pa_u_b_u_c = 0.95

#1
def chon_1_trong_3():
    Pa_n_b_n_c = Pa + Pb + Pc - Pa_u_b - Pa_u_c - Pb_u_c +  Pa_u_b_u_c
    return Pa_n_b_n_c
Pa_n_b_n_c = chon_1_trong_3()
print(f"Xác suất người mua chọn ít nhất 1 trong 3 tiêu chí : {Pa_n_b_n_c}")

#2
def khong_chon_tieu_chi_nao():
    L = 1 - Pa_n_b_n_c
    return L
L = khong_chon_tieu_chi_nao()
print(f"Xác suất người mua không chọn tiêu chí nào : {L}")

#3
def chi_chon_dieu_hoa_nhieu_do():
    Pa_n_c = Pa + Pc - Pa_u_c
    Pb_n_c = Pb + Pc - Pb_u_c
    M = Pc - Pa_n_c - Pb_n_c + Pa_n_b_n_c
    return M
M = chi_chon_dieu_hoa_nhieu_do()    
print(f"Xác suất người mua chỉ chọn tiêu chí điều hòa nhiệt độ : {M}")