import sqlite3

DB_FILE = "MySqlite3.db"

class SqliteUtil:
    @staticmethod
    def create_connection():
        '''Tạo kết nối tới CSDL'''
        try:
            return sqlite3.connect(DB_FILE)
        except Exception as ex:
            print(ex)
            return None
    
    @staticmethod
    def execute(sql_command):
        '''Chạy tác thêm, xóa, sửa'''
        conn = SqliteUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_command)
                conn.commit()
                conn.close()
                return True
            except Exception as ex:
                print(ex)
                return False
        else:
            return False
        
    
    @staticmethod
    def query(sql_query_command):
        '''Lấy dữ liệu'''
        conn = SqliteUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_query_command)
                data = cur.fetchall()
                conn.close()
                return data # dạng list [] các tuple ()
            except Exception as ex:
                print(ex)
                return None
        else:
            return None
        
    @staticmethod
    def insert_and_get_lasted_id(sql_statetement):
        '''Chèn và trả về mã vừa tăng (sinh)'''
        conn = SqliteUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_statetement)
                conn.commit()
                lastid = cur.lastrowid
                conn.close()
                return lastid
            except Exception as ex:
                print(ex)
                return None
        else:
            return None



    
