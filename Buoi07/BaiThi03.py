'''
Viết class Student bao gồm thuộc tính và phương thức sau:
+ Thuộc tính:
name (tên sinh viên dạng chuỗi)
ap_mark, security_mark, web_mark (ap_mark, security_mark, web_mark là điểm 3 môn học: Lập trình nâng cao, Bảo mật, Thiết kế Web với mỗi điểm là một số thực (lấy 1 chữ số))
+ Viết phương thức __init__ khởi tạo
+ Viết phương thức __str__ trả về chuỗi in ra dạng thông tin Student như sau: 
"name, (ap_mark, security_mark, web_mark)"
+ Viết phương thức tính điểm trung bình của 03 môn thi.
+ Viết phương thức tìm điểm thi có giá trị lớn nhất.
+ Viết hàm main để nhập vào mảng thông tin 25 sinh viên lớp mình, xuất ra sinh viên nào có điểm trung bình 3 môn thi lớn nhất.
'''
class Student:
    def __init__(self, name, ap, security, web) -> None:
        self.name = name
        self.ap_mark = ap
        self.security_mark = security
        self.web_mark = web
        
    def __str__(self) -> str:
        return f"{self.name}, AP: {self.ap_mark}, Sec: {self.security_mark}, web: {self.web_mark}"
    
    def average_mark(self):
        return (self.ap_mark + self.security_mark + self.web_mark) / 3
    
    def max_mark(self):
        return max(self.ap_mark, self.security_mark, self.web_mark)
    
if __name__ == "__main__":
    students = []
    while len(students) < 25:
        try:
            # TODO: Input data
            pass
        except:
            print("Chưa hợp lệ")
    
    student_average_mark_max = max(students, lambda student: student.average_mark())
    
    diem_cao_nhat = students[0].average_mark()
    for std in range(1, len(students)):
        if std.average_mark() >= diem_cao_nhat:
            diem_cao_nhat = std.average_mark()
            
    ds_sv_diem_cao_nhat = list(filter(lambda x: x.average_mark() == diem_cao_nhat, students))
    