import matplotlib.pyplot as plt

# S1: Data
xdata = ["A", "B", "C", "D", "F"]
ydata = [11, 22, 10, 2, 1]

# S2: Chọn đồ thị vẽ
plt.plot(xdata, ydata)

# S2': Thêm thông tin cho đồ thị
plt.xlabel("GRADE")
plt.ylabel("Count")
plt.title("Statictics by Grade")

# S3: Hiện đồ thị
plt.show()