## Connect SQLite, Create Table
import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''
             Create table student (
                 st_id INT AUTO_INCREMENT PRIMAR_KEY
                 st_name VARCHAR(50),
                 st_class VARCHAR(10),
                 st_email VARCHAR(30)
                 )
                 ''')
conn.close()                 