# a python implementation of a web server which recognizes data from post requests
# to run: `python salad_server.py`
# source(s):
#   + http://georgik.sinusgear.com/2011/01/07/how-to-dump-post-request-with-python/
#   + https://snipt.net/raw/f8ef141069c3e7ac7e0134c6b58c25bf/?nice

import code # to debug: `code.interact(local=locals())`
import logging # to log: `logging.warning("MY MESSAGE")` or `logging.error("MY MESSAGE")`
import SimpleHTTPServer
import SocketServer
import cgi
import json

PORT = 8818

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.log_message("======= GETTING =======")
        self.log_message("HEADERS: " + json.dumps(dict(self.headers)))
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self.log_message("======= POSTING =======")
        self.log_message("HEADERS: " + json.dumps(dict(self.headers)))

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        form_dict = {}
        for attribute in form.list:
            form_dict[attribute.name] = attribute.value
        self.log_message("POSTED DATA: " + json.dumps(form_dict))

        # TODO: store data in database depending on which page was posted to
        #title = form['title'].value
        #calories = form['calories'].value # int(form['calories'].value)
        #description = form['description'].value

        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "SERVING AT PORT:", PORT
httpd.serve_forever()
