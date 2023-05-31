import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='firefox1', database='menagerie')
cursor = conn.cursor()
select_query = "SELECT * FROM pet"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()