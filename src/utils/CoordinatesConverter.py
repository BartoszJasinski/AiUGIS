from pyproj import Proj, transform
from os import chdir
from xml.dom import minidom

os.chdir()

parsed_districts_borders_data = minidom.parse()


# inProj = Proj(init='epsg:2178')
# outProj = Proj(init='epsg:4326')
# x1,y1 = 7497102.230000,5792599.380000
# x2,y2 = transform(inProj,outProj,x1,y1)
# print(x2,y2)