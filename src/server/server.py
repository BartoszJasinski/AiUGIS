#!/usr/bin/env python3

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.write("Hello, world")


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()




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
