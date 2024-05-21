


import pymysql as mysql # pysql

con = mysql.connect(user='root',password='root', host='localhost',db='School')

print(con)

cur = con.cursor()

# query

query =f'show tables;'

cur.execute(query)

for i in cur:
    print(i)
