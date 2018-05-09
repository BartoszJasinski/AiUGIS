from pyproj import Proj, transform
import os
from xml.dom import minidom

districts_borders_data_path = "../../data"
os.chdir(districts_borders_data_path)

districts_borders_data_file_name = "districts_borders_data.xml"
parsed_districts_borders_data = minidom.parse(districts_borders_data_file_name)

list = parsed_districts_borders_data.getElementsByTagName('gml:coordinates')
for record in list:
    print(record.firstChild.nodeValue, '\n\n\n\n\n')


# inProj = Proj(init='epsg:2178')
# outProj = Proj(init='epsg:4326')
# x1,y1 = 7497102.230000,5792599.380000
# x2,y2 = transform(inProj,outProj,x1,y1)
# print(x2,y2)