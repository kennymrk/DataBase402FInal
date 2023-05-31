import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='firefox1')

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS menagerie")

conn.commit()
cursor.close()
conn.close()