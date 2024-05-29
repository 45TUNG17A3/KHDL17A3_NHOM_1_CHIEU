#phần 1:
import math
n=650
p=0.7
k=439
xac_suat = 0
for i in range(k+1):
    xac_suat +=math.comb(n,i) * (p**i)*(1-p)**(n-i)
print(f"xác suất để số sinh viên đến đọc sách ít hơn 440 là {xac_suat:.4f}")

#phần 2:
n=650 
p=0.7
xac_suat_du_ghe = 0.99
so_ghe = 0
xac_suat_1 = 0
while xac_suat_1 < xac_suat_du_ghe:
    xac_suat_1 += math.comb(n, so_ghe)*(p**so_ghe)*((1-p)**(n-so_ghe))
    so_ghe+=1
    print(f"số ghế cần chuẩn bị là:{so_ghe}")