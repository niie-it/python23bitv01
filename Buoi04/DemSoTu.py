chuoi = input("Nhập chuỗi: ").strip()

# Remove các kí tự đặc biệt
pattern = "[],:!@"
for ki_tu_dac_biet in pattern:
    chuoi = chuoi.replace(ki_tu_dac_biet, "")
    
print("Sau:", chuoi)

arr_words = chuoi.split()
print(arr_words)
print(len(arr_words), "words")