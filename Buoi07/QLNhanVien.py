'''
Viết class NhanVien gồm các thuộc tính:
●	Tên
●	Tuổi
●	Địa chỉ
●	Tiền lương
●	Tổng số giờ làm
'''
class NhanVien:
    def __init__(self, ten, tuoi, dia_chi, luong, so_gio_lam):
        self.HoTen = ten
        self.Tuoi = tuoi
        self.DiaChi = dia_chi
        self.Luong = luong
        self.TongSoGioLam = so_gio_lam
    
    def __str__(self) -> str:
        return f"{self.HoTen}, {self.Tuoi} tuổi, ở {self.DiaChi}"
        
# Demo
nv1 = NhanVien('Lê Tê', 21, '458 Nguyễn Hữu Thọ', 1001, 38)
print(nv1)
print(nv1.HoTen, nv1.Luong)
