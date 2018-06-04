#!/usr/bin/env python3

import csv
import os
from xml.dom import minidom

import numpy
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
        coordinates = {'latitude': float(str(click_coordinates).split(",")[1]),
                       'longitude': float(str(click_coordinates).split(",")[0])}
        district_name = self.getDistrictByCoordinates(coordinates)
        self.write(district_name)
        # TODO district_data = self.getDataForDistrict(district_name)
        # TODO self.write(district_data)

    @staticmethod
    def getDistrictByCoordinates(coordinates):
        current_working_directory = os.getcwd()
        try:
            districts_borders_data_path = "../../data"
            os.chdir(districts_borders_data_path)
            districts_borders_data_file_name = "districts_borders_converted_data.xml"

            parsed_districts_borders_data = minidom.parse(districts_borders_data_file_name)
            districts_coordinates = parsed_districts_borders_data.getElementsByTagName('gml:coordinates')

            district_counter = 0
            for record in districts_coordinates:
                print(record.firstChild.nodeValue.split(" "), '\n\n\n\n\n')
                district_border_coordinates_list = record.firstChild.nodeValue.split(" ")
                latitude_border_coordinates_vector = []
                longitude_border_coordinates_vector = []
                for district_border_coordinate_string in district_border_coordinates_list:
                    district_border_coordinate = district_border_coordinate_string.split(",")
                    latitude_border_coordinates_vector.append(float(district_border_coordinate[1]))
                    longitude_border_coordinates_vector.append(float(district_border_coordinate[0]))

                lons_lats_vect = numpy.column_stack(
                    (latitude_border_coordinates_vector, longitude_border_coordinates_vector))  # Reshape coordinates
                polygon = Polygon(lons_lats_vect)  # create polygon
                point = Point(coordinates['latitude'], coordinates['longitude'])  # create point
                if polygon.contains(point):
                    return parsed_districts_borders_data.getElementsByTagName('ns92528565:DZIELNICA')[district_counter]\
                        .firstChild.nodeValue  # District name
                district_counter += 1

            return 'Unknown_District'
        finally:
            os.chdir(current_working_directory)

    @staticmethod
    def getDataForDistrict(district_name):
        # dirname = os.path.dirname(__file__)
        # filename = os.path.join(dirname, '..', 'data', '')
        os.chdir("../../data/")
        print(os.getcwd() + "\n")
        with open('Warsaw_districts_data.csv', 'r') as csv_file:
            csv_districts_data = csv.reader(csv_file, delimiter=',')
            for record in csv_districts_data:
                print(record["ID_Key"])
                # if record["District_Name"] == district_name:
                #     return record['District_Name']


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