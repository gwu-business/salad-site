# a python implementation of a local web server which
# ... recognizes web form data from post requests
# ... and stores web form data in a mysql database.
# to run from root dir: `python software/start_local_web_server.py`
# source(s):
#   + http://georgik.sinusgear.com/2011/01/07/how-to-dump-post-request-with-python/
#   + https://snipt.net/raw/f8ef141069c3e7ac7e0134c6b58c25bf/?nice
#   + https://github.com/PyMySQL/PyMySQL#example

import code # to debug: `code.interact(local=locals())`
import logging # to log: `logging.warning("MY MESSAGE")` or `logging.error("MY MESSAGE")`
import SimpleHTTPServer
import SocketServer
import cgi
import json
#import urlparse
import pymysql.cursors

PORT = 8818

# DEFINE THE LOCAL WEB SERVER

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if ".html" in self.path: # only log messages for html pages, not images and scripts
            self.log_message("GETTING: " + self.path)
            self.log_message("HEADERS: " + json.dumps(dict(self.headers)))
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.log_message("POSTING: " + self.path)
        self.log_message("HEADERS: " + json.dumps(dict(self.headers)))

        # READ FORM DATA

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # LOG FORM DATA

        form_dict = {}
        for attribute in form.list:
            form_dict[attribute.name] = attribute.value
        self.log_message("POSTED DATA: " + json.dumps(form_dict))

        # IF POSTING TO THE NEW MENU ITEMS PATH, CREATE A NEW MENU ITEM RECORD IN THE DATABASE

        if self.path == "/menu-items/new.html":
            self.log_message("STORING: " + json.dumps(form_dict))

            # TRANSFORM DATA

            category = "SpecialSalad"
            title = form['title'].value
            calories = form['calories'].value
            calories = int(calories)
            contains_gluten = True
            vegan_safe = False
            description = form['description'].value

            # ESTABLISH DATABASE CONNECTION

            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='y0l0', # or change, or leave blank or comment-out
                db='salad_db',
                #charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            # EXECUTE DATABASE TRANSACTION

            try:

                # CREATE NEW RECORD

                with connection.cursor() as cursor:
                    sql = "INSERT INTO `menu_items` (`category`,`title`,`calories`,`contains_gluten`,`vegan_safe`,`description`) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (category, title, calories, contains_gluten, vegan_safe, description)  )
                connection.commit() # to save the changes

                # PRINT NEW RECORD

                with connection.cursor() as cursor:
                    sql = "SELECT * FROM menu_items ORDER BY id DESC LIMIT 1"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    print(result)

            finally:
                connection.close() # for performance

            self.log_message("STORED")

            # REDIRECT TO MENU INDEX

            self.log_message("REDIRECTING")
            self.send_response(301)
            self.send_header('Location',"/menu-items/index.html")
            self.end_headers()

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

# RUN THE LOCAL WEB SERVER

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "SERVING AT PORT:", PORT
httpd.serve_forever()
