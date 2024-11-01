# Đếm số nguyên âm
nguyen_am = "ueoai"

chuoi = input("Nhập chuỗi: ").strip()

count = 0
for ki_tu in chuoi:
    if ki_tu in nguyen_am:
        count += 1
    
print(count, 'nguyên âm')