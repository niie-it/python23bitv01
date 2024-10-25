'''
Count the total number of digits in a number
Example, the number is 75869, so the output should be 5
Đếm số chữ số và tổng các chữ số
Input: N = 19001080
Output: count = 8, sum = 19
'''
while True:
    chuoi_so = input("Nhập số: ")
    if chuoi_so.isnumeric():
        break
    print("Không phải số. Nhập lại!!!")

# Cách 1
sum = 0
for ki_so in chuoi_so:
    sum += int(ki_so)
print(f"{chuoi_so} có tổng các chữ số là {sum}")

# Cách 2
sum2 = 0
so = int(chuoi_so)
while so > 0:
    sum2 += so % 10
    so = so // 10

print(f"{chuoi_so} có tổng các chữ số là {sum2}")



