import math

lambda_1 = 2

def bon_o_to_duoc_thue(): # P(X = 4)
    A = ((lambda_1 ** 4) * ((math.e) ** -(lambda_1))) / (math.factorial(4))
    return A
A = bon_o_to_duoc_thue()
print(f"Xác suất bốn ô tô được thuê là : {A}")


def bon_o_to_khong_duoc_thue():
    B = 1 - A
    return B
B = bon_o_to_khong_duoc_thue()
print(f"Xác suất để 4 chiếc ô tô không được thuê là : {B}")


def cua_hang_khong_dap_ung_yeu_cau(): # P(X > 4)
    P_0 = ((lambda_1 ** 0) * ((math.e) ** -(lambda_1))) / (math.factorial(0))
    P_1 = ((lambda_1 ** 1) * ((math.e) ** -(lambda_1))) / (math.factorial(1))
    P_2 = ((lambda_1 ** 2) * ((math.e) ** -(lambda_1))) / (math.factorial(2))
    P_3 = ((lambda_1 ** 3) * ((math.e) ** -(lambda_1))) / (math.factorial(3))
    P_4 = ((lambda_1 ** 4) * ((math.e) ** -(lambda_1))) / (math.factorial(4))
    C = 1 - (P_0 + P_1 + P_2 + P_3 + P_4)
    return C
C = cua_hang_khong_dap_ung_yeu_cau()
print(f"Xác suất cửa hàng không đáp ứng yêu cầu là : {C}")




def trung_binh_o_to_duoc_thue():
    D = lambda_1
    return D
D = trung_binh_o_to_duoc_thue()
print(f"Trung bình ô tô được thuê là : {D}")