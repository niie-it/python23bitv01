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
        return f"{self.HoTen}, {self.Tuoi} tuổi, ở {self.DiaChi}, ${self.Luong}, thưởng {self.tinh_thuong()}, tổng: {self.Luong + self.tinh_thuong()}"
    
    def tinh_thuong(self):
        if self.TongSoGioLam >= 200: return self.Luong * 0.2
        if self.TongSoGioLam >= 100: return self.Luong * 0.1
        return 0
        
# Demo
nv1 = NhanVien('Lê Tê', 21, '458 Nguyễn Hữu Thọ', 2000, 38)
# print(nv1)
# print(nv1.HoTen, nv1.Luong)

ds_nhan_vien = []
ds_nhan_vien.append(nv1)
nv2 = NhanVien('Lý Lê La', 22, '123 Lê Lợi', 1909, 200)
ds_nhan_vien.append(nv2)

nv_co_luong_cao_nhat = ds_nhan_vien[0]
for nv in ds_nhan_vien:
    print(nv)
    if (nv.Luong + nv.tinh_thuong() > nv_co_luong_cao_nhat.Luong + nv_co_luong_cao_nhat.tinh_thuong()):
        nv_co_luong_cao_nhat = nv
        
print("NV có lương cao nhất là:", nv_co_luong_cao_nhat)