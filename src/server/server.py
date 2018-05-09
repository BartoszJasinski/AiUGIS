#!/usr/bin/env python3

import socketserver
import os

from http.server import BaseHTTPRequestHandler, http


PORT = 8888
DATA_LOCATION = "../../data"


class HttpRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        index = open("./index.html", 'rb')
        self.wfile.write(index.read())


    def do_HEAD(self):
        data = open("Warsaw_districts_population.csv", "rb")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data.read())


with socketserver.TCPServer(('', PORT), HttpRequestHandler) as httpd:
    print("serving at port", PORT)
    # os.chdir(DATA_LOCATION)
    httpd.serve_forever()
