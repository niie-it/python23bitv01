# Đếm số nguyên âm
nguyen_am = "ueoai"

chuoi = input("Nhập chuỗi: ").strip()

# Làm sao đây>
# Muốn số từng loại {"a": 5, "o": 8}
thong_ke = {}
for ki_tu in nguyen_am:
    thong_ke[ki_tu] = chuoi.count(ki_tu)
    
print(thong_ke)