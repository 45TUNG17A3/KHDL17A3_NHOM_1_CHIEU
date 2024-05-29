# Hàm biểu diễn biến cố có đúng một sinh viên đạt yêu cầu
def exactly_one_student_passes(B):
    return (B[0] and not B[1] and not B[2] and not B[3]) or \
           (not B[0] and B[1] and not B[2] and not B[3]) or \
           (not B[0] and not B[1] and B[2] and not B[3]) or \
           (not B[0] and not B[1] and not B[2] and B[3])

# Hàm biểu diễn biến cố có đúng ba sinh viên đạt yêu cầu
def exactly_three_students_passes(B):
    return (B[0] and B[1] and B[2] and not B[3]) or \
           (B[0] and B[1] and not B[2] and B[3]) or \
           (B[0] and not B[1] and B[2] and B[3]) or \
           (not B[0] and B[1] and B[2] and B[3])

# Hàm biểu diễn biến cố có ít nhất một sinh viên đạt yêu cầu
def at_least_one_student_passes(B):
    return B[0] or B[1] or B[2] or B[3]

# Hàm biểu diễn biến cố không có sinh viên nào đạt yêu cầu
def no_student_passes(B):
    return not B[0] and not B[1] and not B[2] and not B[3]

# Ví dụ các kết quả của các sinh viên (đạt yêu cầu hoặc không)
B = [True, False, True, False]

# Kiểm tra các biến cố
print(f"Có đúng một sinh viên đạt yêu cầu: {exactly_one_student_passes(B)}")
print(f"Có đúng ba sinh viên đạt yêu cầu: {exactly_three_students_passes(B)}")
print(f"Có ít nhất một sinh viên đạt yêu cầu: {at_least_one_student_passes(B)}")
print(f"Không có sinh viên nào đạt yêu cầu: {no_student_passes(B)}")