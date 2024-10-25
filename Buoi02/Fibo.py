'''In n phần tử dãy Fibonaci'''
arr = []
n = int(input("Nhập số phần tử: "))
if n < 0:
    print("Không hợp lệ")
else:
    for idx in range(n): # n = 0,1,...,n-1
        if idx in [0, 1]:
            arr.append(1)
        else:
            arr.append(arr[idx - 1] + arr[idx - 2])
            
print(arr)
        