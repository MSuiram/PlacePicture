import folium
import os
from marker_maker import marker_maker
from coord import coord_calculator

my_map = folium.Map()

path_name = 'path'
images = [img for img in os.listdir(path_name) if img.endswith(".jpg")]
print(images)

for image in images:
    coord = coord_calculator(path_name + "/" + image)
    if coord is not None:
        print(image)
        marker_maker(my_map, coord, image)


my_map.save("my_map.html")
