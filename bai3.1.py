import math
p = 0.1
n = 5

#1 Dùng phân phối nhị thức
k = 2
def mot_ngay_2_may_hong():
    Xac_suat_hong_may = (math.factorial(n)/ (math.factorial(k) * math.factorial(n - k)) ) * (p ** 2) * ( (1 - p) ** 3 )
    return Xac_suat_hong_may
Xac_suat_hong_may = mot_ngay_2_may_hong()
print(f"Xác suất 1 ngày hỏng 2 máy : {Xac_suat_hong_may}")
    
    
#2 Dùng phân phối nhị thức
k1 = 0
k2 = 1
k3 = 2
def mot_ngay_khong_qua_2_may_hong():
    P1 = (math.factorial(n) / (math.factorial(k1) * math.factorial(n - k1)) ) * (p ** k1) * ((1 - p) ** (n - k1))
    P2 = (math.factorial(n) / (math.factorial(k2) * math.factorial(n - k2)) ) * (p ** k2) * ((1 - p) ** (n - k2))
    P3 = (math.factorial(n) / (math.factorial(k3) * math.factorial(n - k3)) ) * (p ** k3) * ((1 - p) ** (n - k3))      
    Xac_suat_1_ngay_khong_qua_2_may_hong = P1 + P2 + P3
    return Xac_suat_1_ngay_khong_qua_2_may_hong
Xac_suat_1_ngay_khong_qua_2_may_hong = mot_ngay_khong_qua_2_may_hong()
print(f"Xác suất 1 ngày không quá 2 máy hỏng : {Xac_suat_1_ngay_khong_qua_2_may_hong}")