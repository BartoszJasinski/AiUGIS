#!/usr/bin/env python3

import socketserver
import os

from http.server import BaseHTTPRequestHandler, http



# Handler = http.server.SimpleHTTPRequestHandler
PORT = 8888
DATA_LOCATION = "../../data"


class HttpRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # data = open("Warsaw_districts_population.csv", "rb")
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(data.read())

        self.send_response(200)
        self.end_headers()
        index = open("./index.html", 'rb')
        self.wfile.write(index.read())


with socketserver.TCPServer(('', PORT), HttpRequestHandler) as httpd:
    print("serving at port", PORT)
    # os.chdir(DATA_LOCATION)
    httpd.serve_forever()
# httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
# httpd.serve_forever()




# # !/usr/bin/env python
# """
# Very simple HTTP server in python.
# Usage::
#     ./dummy-web-server.py [<port>]
# Send a GET request::
#     curl http://localhost
# Send a HEAD request::
#     curl -I http://localhost
# Send a POST request::
#     curl -d "foo=bar&bin=baz" http://localhost
# """
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# import SocketServer
#
#
# class S(BaseHTTPRequestHandler):
#     def _set_headers(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#
#     def do_GET(self):
#         self._set_headers()
#         self.wfile.write("<html><body><h1>hi!</h1></body></html>")
#
#     def do_HEAD(self):
#         self._set_headers()
#
#     def do_POST(self):
#         # Doesn't do anything with posted data
#         self._set_headers()
#         self.wfile.write("<html><body><h1>POST!</h1></body></html>")
#
#
# def run(server_class=HTTPServer, handler_class=S, port=80):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print 'Starting httpd...'
#     httpd.serve_forever()
#
#
# if __name__ == "__main__":
#     from sys import argv
#
#     if len(argv) == 2:
#         run(port=int(argv[1]))
#     else:
#         run()


# import tornado.httpserver
# import tornado.ioloop
# import tornado.options
# import tornado.web
#
# from tornado.options import define, options



# define("port", default=8888, help="run on the given port", type=int)
#
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#
#         self.write("Hello, world")
#
#
# def main():
#     tornado.options.parse_command_line()
#     application = tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#     http_server = tornado.httpserver.HTTPServer(application)
#     http_server.listen(options.port)
#     tornado.ioloop.IOLoop.current().start()
#
#
# if __name__ == "__main__":
#     main()




# import http.server
# import socketserver
#
# PORT = 8081
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(('', PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
#
#
