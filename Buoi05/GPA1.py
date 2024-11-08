
def nhap_diem(ten_loai_diem):
    while True:
        try:
            diem = float(input(f"Nhập điểm {ten_loai_diem}: "))
            if 0 <= diem <= 10:
                return diem
                # break
            else:
                print("Điểm nằm trong [0, 10]. Nhập lại!")
        except:
            print("Phải nhập điểm số")
        
qua_trinh = nhap_diem("quá trình")
giua_ky = nhap_diem("giữa kỳ")
cuoi_ky = nhap_diem("cuối kỳ")

final_score = round(qua_trinh * 0.2 + giua_ky * 0.2 + cuoi_ky * 0.6, 1)

gpa = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

def convert_to_gpa(diem):
    if diem >= 8.5: return "A"
    if diem >= 7: return "B"
    if diem >= 5.5: return "C"
    if diem >= 4: return "D"
    return "F"

print("Final score:", final_score, "GPA:", convert_to_gpa(final_score))