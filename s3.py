import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='firefox1')
cursor = conn.cursor()
cursor.close()
conn.close()