import tkinter as tk
from tkinter import StringVar
from tkinter.messagebox import showinfo

# 1. Khai báo màn hình chính
root = tk.Tk()
root.geometry('400x150')
root.title("DEMO TKINTER")

ten_ban = StringVar()
def chao():
    showinfo("Thông báo", f"Xin chào: {ten_ban.get()}")
    
# 2. Gắn các control (widget) vô màn hình chính
tk.Label(root, text="Nhập tên:").pack()
tk.Entry(root, textvariable=ten_ban).pack()
tk.Button(root, text="Chào", command=chao).pack()

# Hiện màn hình
root.mainloop()