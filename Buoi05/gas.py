# Đọc dữ liệu từ file gasin.txt
# Tính giá trung bình từng nước
with open("gasin.txt") as myf:
    lines = myf.readlines()
    gas_usa = []
    gas_bel = []
    for line in lines:
        arr = line.split()
        print(arr)
        gas_usa.append(float(arr[0]))
        gas_bel.append(float(arr[1]))
        
with open("gasout.txt", "w") as mf:
    mf.write(f"USA: {sum(gas_usa)/len(gas_usa)}\n")
    mf.write(f"Beligum: {sum(gas_bel)/len(gas_bel)}\n")