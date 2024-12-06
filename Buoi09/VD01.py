import tkinter as tk

# 1. Khai báo màn hình chính
root = tk.Tk()
root.geometry('400x150')
root.title("DEMO TKINTER")

# 2. Gắn các control (widget) vô màn hình chính
# Mỗi control (widget) có thể gắn sự kiện
# VD gắn label lên màn hình
tk.Label(root, text="Hello, World!").pack()
tk.Entry(root).pack()
tk.Button(root, text="CLICK CK").pack()

# Hiện màn hình
root.mainloop()