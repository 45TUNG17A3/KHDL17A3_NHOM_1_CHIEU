import math

def norm_cdf(x, chieu_cao_trung_binh=0, std=1):
    z = (x - chieu_cao_trung_binh) / std
    t = 1 / (1 + 0.2316419 * abs(z))
    d = 0.3989423 * math.exp(-z * z / 2)
    prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))))
    if z > 0:
        return 1 - prob
    else:
        return prob

chieu_cao_trung_binh = 175
do_lech_chuan = 4

# 1. Tỉ lệ người trưởng thành có tầm vóc trên 180 cm
z_180 = (180 - chieu_cao_trung_binh) / do_lech_chuan
prob_above_180 = 1 - norm_cdf(180, chieu_cao_trung_binh, do_lech_chuan)

# 2. Tỉ lệ người trưởng thành có chiều cao từ 166 cm đến 177 cm
z_166 = (166 - chieu_cao_trung_binh) / do_lech_chuan
z_177 = (177 - chieu_cao_trung_binh) / do_lech_chuan
prob_between_166_177 = norm_cdf(177, chieu_cao_trung_binh, do_lech_chuan) - norm_cdf(166, chieu_cao_trung_binh, do_lech_chuan)

# 3. Phần trăm người có chiều cao dưới mức h0
percent_below_h0 = 0.33
z_value = norm_cdf(percent_below_h0)
h0 = chieu_cao_trung_binh + z_value * do_lech_chuan

prob_above_180, prob_between_166_177, percent_below_h0

print(f"Xác suất người có chiều cao trên 180cm : {prob_above_180}")
print(f"Xác suất người có chiều cao từ 166 cm đến 177 cm : {prob_between_166_177}")
print(f"Xác suất người trưởng thành có chiều cao dưới mức h0 :{percent_below_h0}")


