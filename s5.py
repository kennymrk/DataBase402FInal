import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='firefox1')

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()

for database in databases:
    print(database[0])
    
cursor.close()
conn.close()