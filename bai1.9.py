p1 = 0.5
p2 = 0.4
p12 = 0.1

def xac_suat_trung_it_nhat_1_du_an(p1,p2,p12):
    A = p1 + p2 - p12
    return A
A = xac_suat_trung_it_nhat_1_du_an(p1,p2,p12)
print(f"Xac suat trung it nhat 1 du an la : {A}")



def xac_suat_trung_dung_1_du_an(p1,p2,p12):
    p1_not_p2 = p1 * (1 - p2)
    p2_not_p1 = p2 * (1 - p1)
    chi_p1_hoac_p2 = p1_not_p2 + p2_not_p1
    return chi_p1_hoac_p2
chi_p1_hoac_p2 = xac_suat_trung_dung_1_du_an(p1,p2,p12)
print(f"Xac suat trung dung 1 du an la : {chi_p1_hoac_p2}")



def xac_suat_trung_du_an_2_va_da_trung_thau_du_an_1(p1,p2,p12):
    trung_p2_va_da_trung_p1 = p12 / p1
    return trung_p2_va_da_trung_p1
trung_p2_va_da_trung_p1 = xac_suat_trung_du_an_2_va_da_trung_thau_du_an_1(p1,p2,p12)
print(f"Xac suat trung du an 2 va trung ca du an 1 la : {trung_p2_va_da_trung_p1}")


def xac_suat_trung_du_an_2_khong_trung_du_an_1(p1,p2,p12):
    p2_not_p1 = p2 * (1 - p1)
    return p2_not_p1
p2_not_p1 = xac_suat_trung_du_an_2_khong_trung_du_an_1(p1,p2,p12)
print(f"Xac suat trung du an 2 ma khong trung du an 1 la : {p2_not_p1}")