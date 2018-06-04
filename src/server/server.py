#!/usr/bin/env python3

# import socketserver
# import os
#
# from http.server import BaseHTTPRequestHandler, http
#
#
# PORT = 8887
# DATA_LOCATION = "../../data"
#
#
# class HttpRequestHandler(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         index = open("./index.html", 'rb')
#         self.wfile.write(index.read())
#
#     def do_HEAD(self):
#         data = open("Warsaw_districts_population.csv", "rb")
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(data.read())
#
#
# with socketserver.TCPServer(('', PORT), HttpRequestHandler) as httpd:
#     print("serving at port", PORT)
#     # os.chdir(DATA_LOCATION)
#     httpd.serve_forever()



import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class SiteHandler(tornado.web.RequestHandler):
    def get(self):
        index = open("./index.html", 'rb')
        self.write(index.read())


class ClickHandler(tornado.web.RequestHandler):
    def get(self, click_coordinates):
        click_coordinates = 2339810.58715388,6825327.693052984
        district_name = self.getDistrictByCoordinates(click_coordinates)
        self.write(district_name)

    def getDistrictByCoordinates(self, click_coordinates):
        lons_lats_vect = np.column_stack((lons_vect, lats_vect))  # Reshape coordinates
        polygon = Polygon(lons_lats_vect)  # create polygon
        point = Point(y, x)  # create point
        print(polygon.contains(point))  # check if polygon contains point
        return 'Unknown_District'


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", SiteHandler),
        (r"/([^/]*)", ClickHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()