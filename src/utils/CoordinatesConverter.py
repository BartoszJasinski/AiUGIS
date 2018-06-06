from pyproj import Proj, transform
import osfg
from xml.dom import minidom


districts_borders_data_path = "../../data"
os.chdir(districts_borders_data_path)

districts_borders_data_file_name = "districts_borders_data.xml"
districts_borders_converted_data_file_name = "districts_borders_converted_data.xml"

parsed_districts_borders_data = minidom.parse(districts_borders_data_file_name)

districts_coordinates = parsed_districts_borders_data.getElementsByTagName('gml:coordinates')

for record in districts_coordinates:
    print(record.firstChild.nodeValue.split(" "), '\n\n\n\n\n')
    coordinates_list = record.firstChild.nodeValue.split(" ")
    district_coordinates_converted = ""
    for coordinate in coordinates_list:
        input_projection = Proj(init='epsg:2178')
        output_projection = Proj(init='epsg:3857')
        xy = coordinate.split(",")
        x2, y2 = transform(input_projection, output_projection, xy[0], xy[1])
        district_coordinates_converted += str(x2) + "," + str(y2) + " "
        # print("x2 = ", x2, "  y2 = ", y2)
    district_coordinates_converted = district_coordinates_converted[:-1]
    # print(district_coordinates_converted)
    record.firstChild.replaceWholeText(district_coordinates_converted)
    print(record.firstChild.nodeValue)
    print("\n")
    # print(x2,y2)

# print(parsed_districts_borders_data.getElementsByTagName('gml:coordinates'))
districts_shapes = parsed_districts_borders_data.getElementsByTagName('ns92528565:SHAPE')
for record in districts_shapes:
    record.firstChild.setAttribute('srsName', 'EPSG:3857')

districts_borders_converted_data_file = open(districts_borders_converted_data_file_name, 'w')
parsed_districts_borders_data.writexml(districts_borders_converted_data_file)
# districts_borders_converted_data_file.write(str(list))
