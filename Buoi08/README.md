# Buổi 08: Làm việc database SQLite

- Có thể thiết database trực tiếp trên các tool:
  https://sqliteonline.com/

- template mẫu:

  ```
    import sqlite3
    # Step 1
    connection = sqlite3.connect("QLHocVien.db")

    # step 2
    cursor = connection.cursor()

    # step 3
    cursor.execute("SQL statement")

    # step 4
    connection.close()
  ```
