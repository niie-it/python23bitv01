"""
BT02: Nhập dài, rộng HCN
Xuất diện tích, chu vi
"""
while True:
    dai = float(input("Nhập chiều dài HCN: "))
    rong = float(input("Nhập chiều rộng HCN: "))
    if dai > 0 and rong > 0:
        break # Thoát vòng lặp
    else:
        print("Dữ liệu không hợp lệ. Nhập lại!!!")
        
print("HCN dai=", dai, "rộng=", rong, "S=", dai*rong,
      "P=", (dai+rong)*2)
