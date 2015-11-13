import pymysql # https://github.com/PyMySQL/PyMySQL

# OPEN THE DB CONNECTION

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='y0l0') # , db='mysql'
cursor = connection.cursor()

# EXECUTE A QUERY

cursor.execute("SELECT * FROM mysql.user;")

# LOG QUERY RESULTS

print type(cursor)
print cursor
print cursor.description
print cursor.fetchall()
num_fields = len(cursor.description)
print num_fields

field_names = [i[0] for i in cursor.description]
print field_names

for row in cursor.fetchall():
   print(row)

# CLOSE THE DB CONNECTION

cursor.close()
connection.close()
