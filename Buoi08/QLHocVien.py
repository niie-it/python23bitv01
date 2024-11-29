import sqlite3

try:
    # Step 1
    connection = sqlite3.connect("QLHocVien.db")

    # step 2
    cursor = connection.cursor()

    # step 3
    # sql_create_table = '''CREATE TABLE HocVien
    # (
    #     MaHV text PRIMARY KEY,
    #     HoTen text,
    #     DienThoai text,
    #     NgaySinh date,
    #     Email text
    # )'''
    # cursor.execute(sql_create_table)
    
    # sql_insert = '''
    # INSERT INTO HocVien(MaHV, HoTen, DienThoai, NgaySinh, Email)
    # VALUES('HV010', 'Ly Trần', '0989123456', '01/01/2000', 'ly.tran@tt.info')
    # '''
    # cursor.execute(sql_insert)
    
    # Lấy ra
    sql_select = "SELECT * FROM HocVien"
    cursor.execute(sql_select)
    results = cursor.fetchall()
    for p in results:
        print(p)

    # đánh dấu thay đổi dữ liệu
    # connection.commit() # Chỉ dành cho insert, update, delete
except Exception as ex:
    print('Error', ex)
finally:
    # step 4
    if connection:
        connection.close()