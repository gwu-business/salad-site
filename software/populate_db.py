# python software/populate_db.py
# ... source: https://github.com/PyMySQL/PyMySQL#example

import pymysql.cursors

# ESTABLISH CONNECTION WITH SALAD DATABASE

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='y0l0', # or change, or leave blank
    db='salad_db',
    #charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        # CREATE A NEW MENU ITEM RECORD

        sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`contains_gluten`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, ('SignatureSalad', 'TEST SALAD',  1111, 0, 1,  'a salad to use when testing the web application.')  )

    connection.commit() # connection is not autocommit by default. So you must commit to save your changes.

    with connection.cursor() as cursor:

        # EXECUTE CUSTOM QUERY TO FIND THE LATEST MENU ITEM RECORD

        sql = "SELECT * FROM menu_items ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        #result = cursor.fetchone()
        for row in cursor.fetchall():
           print(row)

finally:
    connection.close() # always close the connection when finished.



















##import pymysql # https://github.com/PyMySQL/PyMySQL
##
### OPEN THE DB CONNECTION
##
##connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='y0l0') # , db='mysql'
##cursor = connection.cursor()
##
### EXECUTE A QUERY
##
##cursor.execute("SELECT * FROM mysql.user;")
##
### LOG QUERY RESULTS
##
##print type(cursor)
##print cursor
##print cursor.description
##print cursor.fetchall()
##num_fields = len(cursor.description)
##print num_fields
##
##field_names = [i[0] for i in cursor.description]
##print field_names
##
##for row in cursor.fetchall():
##   print(row)
##
### CLOSE THE DB CONNECTION
##
##cursor.close()
##connection.close()
