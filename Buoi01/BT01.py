'''Nhập vào tên, năm sinh xuất ra tuổi'''
ho_ten = input("Nhập họ tên: ").strip()
nam_sinh = int(input("Năm bạn sinh: ").strip())

print("Bạn", ho_ten, "sinh năm", nam_sinh, ",", 2024 - nam_sinh, "tuổi")