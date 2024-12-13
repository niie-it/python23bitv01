"""
Chương trình QLSV bao gồm: Thêm, xóa, sửa, tìm ds sinh viên;
B1/ Đn dữ liệu SV trong file students.json
B2/ Thiết kế giao diện
"""
import json
import os
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

main = tk.Tk()
main.title("Quản lý sinh viên v.0.0.1")
# main.geometry("400x500")

FILE_PATH = "students.json"

def load_student_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_student_data():
    with open(FILE_PATH, 'w') as file:
        json.dump(students_data, file, indent=4)

students_data = load_student_data()

def them_sinh_vien():
    if not student_id.get() or not full_name.get() or not mark.get():
        showwarning("Lỗi", "Chưa nhập dữ liệu")
        return
    # validate mark
    # 1/ điểm hợp lệ
    try:
        mark_data = float(mark.get())
        if mark_data < 0 or mark_data > 10:
            raise Exception("Điểm là số thực từ 0 --> 10")
    except ValueError:
        showwarning("Lỗi", "Điểm là số thực")
        return
    except Exception as ex:
        showwarning("Lỗi", ex)
        return
    # 2/ mã  đã có hay chưa
    
    students_data.append({
        "id": int(student_id.get()),
        "full_name": full_name.get(),
        "gender": gender.get(),
        "mark": mark_data,
        "gpa": "A"
    })
    print("After add new student:", students_data)
    save_student_data()
    update_student_list()
    clear_input()

def update_student():
    id = student_id.get()
    name = full_name.get()
    mark_value = mark.get()

    # Check existed student

    # Check valid mark
    
    # update student_data

# Function to delete student
def delete_student():
    # Check existed student

    # Check valid mark
    
    # delete student
    pass

def update_student_list():
    listbox_students.delete(0, tk.END)
    for std in students_data:
        listbox_students.insert(tk.END, f"{std['id']}: {std['full_name']} - {std['mark']} - {std['gpa']}")
        
def clear_input():
    student_id.delete(0, tk.END)
    full_name.delete(0, tk.END)
    mark.delete(0, tk.END)

# Gắn control
tk.Label(main, text= "QUẢN LÝ SINH VIÊN", font="Arial 25").grid(row=0, column=1)
tk.Label(main, text= "Mã", padx=10, pady=5).grid(row=1, column=0)
student_id = tk.Entry(main)
student_id.grid(row=1, column=1)
tk.Label(main, text= "Họ tên", padx=10, pady=5).grid(row=2, column=0)
full_name = tk.Entry(main)
full_name.grid(row=2, column=1)
tk.Label(main, text= "Điểm", padx=10, pady=5).grid(row=3, column=0)
mark = tk.Entry(main)
mark.grid(row=3, column=1)


gender = tk.StringVar()
r1 = tk.Radiobutton(main, text='Nam', value='0', variable=gender)
r2 = tk.Radiobutton(main, text='Nữ', value='1', variable=gender)
r1.grid(row=4, column=0)
r2.grid(row=4, column=1)

tk.Button(main, text="Thêm", padx=5, pady=5, command=them_sinh_vien).grid(row=5, column=0)
tk.Button(main, text="Sửa", padx=5, pady=5).grid(row=5, column=1)
tk.Button(main, text="Xóa", padx=5, pady=5).grid(row=6, column=0)
tk.Button(main, text="Lấy", padx=5, pady=5, command=update_student_list).grid(row=6, column=1)

listbox_students = tk.Listbox(main, height=10, width=50)
listbox_students.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

main.mainloop()