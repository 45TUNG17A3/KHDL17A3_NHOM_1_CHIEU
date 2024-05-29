khong_gian_mau_mot_lan_tung = [1, 2, 3, 4, 5, 6]
print("Không gian mẫu khi quan sát một lần tung:", khong_gian_mau_mot_lan_tung)

n = int(input("Nhập số lần tung: "))
while n<=0:
    n = int(input("Số lần tung không hợp lệ, hãy nhập lại: "))
khong_gian_mau_den_khi_xuat_hien_luc = list(range(1, n+1))
print("Không gian mẫu khi xem xét số lần tung cho đến khi xuất hiện mặt 'lục' là:", khong_gian_mau_den_khi_xuat_hien_luc)