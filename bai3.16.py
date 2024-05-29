import math

# Hàm gần đúng cho hàm phân phối tích lũy nghịch đảo (erfinv)
def erfinv(y):
    a = 0.147  # Hằng số sử dụng trong công thức gần đúng
    part1 = 2/(math.pi * a) + math.log(1-y**2)/2
    part2 = math.log(1-y**2)/a
    return math.copysign(math.sqrt(math.sqrt(part1**2 - part2) - part1), y)

# Hàm tính giá trị Z của phân phối chuẩn
def z_value(x, mean, std_dev):
    return (x - mean) / std_dev

# Hàm tính xác suất tích lũy của phân phối chuẩn tại giá trị z
def phi(z):
    # Sử dụng công thức của hàm phân phối tích lũy cho phân phối chuẩn
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

# 1) Tính tỉ lệ sản phẩm phải bảo hành, nếu quy định thời gian bảo hành sản phẩm là 980 giờ.
mean_lifetime = 1000  # Tuổi thọ trung bình
std_dev_lifetime = 10  # Độ lệch chuẩn
warranty_time = 980  # Thời gian bảo hành

# Tính giá trị Z cho thời gian bảo hành
z_warranty = z_value(warranty_time, mean_lifetime, std_dev_lifetime)

# Tính tỉ lệ sản phẩm phải bảo hành
warranty_rate = phi(z_warranty)

print(f"Tỉ lệ sản phẩm phải bảo hành (nếu bảo hành trong {warranty_time} giờ): {warranty_rate * 100:.2f}%")

# 2) Muốn tỉ lệ sản phẩm phải bảo hành là 1% thì phải quy định thời gian bảo hành là bao nhiêu giờ?

# Xác suất tích lũy phi(z) = 1% = 0.01
target_warranty_rate = 0.01

# Tìm giá trị z từ phi(z)
z_target = math.sqrt(2) * erfinv(2 * target_warranty_rate - 1)

# Tính thời gian bảo hành tương ứng
warranty_time_target = mean_lifetime + z_target * std_dev_lifetime

print(f"Thời gian bảo hành để tỉ lệ bảo hành là 1%: {warranty_time_target:.2f} giờ")

# 3) Tính lợi nhuận kỳ vọng khi bán mỗi sản phẩm

profit_per_product = 150000  # Lợi nhuận trên mỗi sản phẩm
cost_per_warranty = 500000  # Chi phí khi bảo hành

# Tỉ lệ sản phẩm phải bảo hành tính ở câu 1
expected_profit = profit_per_product - warranty_rate * cost_per_warranty

print(f"Lợi nhuận kỳ vọng khi bán mỗi sản phẩm: {expected_profit:.2f} đồng")

# 4) Nếu muốn lợi nhuận kỳ vọng là 45 ngàn đồng thì phải quy định thời gian bảo hành là bao nhiêu giờ?

# Lợi nhuận kỳ vọng mong muốn
target_expected_profit = 45000

# Tính tỉ lệ bảo hành mong muốn
target_warranty_rate = (profit_per_product - target_expected_profit) / cost_per_warranty

# Tìm giá trị z tương ứng với tỉ lệ bảo hành mong muốn
z_target_profit = math.sqrt(2) * erfinv(2 * target_warranty_rate - 1)

# Tính thời gian bảo hành tương ứng
warranty_time_for_target_profit = mean_lifetime + z_target_profit * std_dev_lifetime

print(f"Thời gian bảo hành để lợi nhuận kỳ vọng là 45 ngàn đồng: {warranty_time_for_target_profit:.2f} giờ")