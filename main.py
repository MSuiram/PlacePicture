import folium
import os
import webbrowser
from marker_maker import marker_maker
from coord import coord_calculator
from secret import path

my_map = folium.Map()

path_name = path
images = [img for img in os.listdir(path_name) if img.endswith(".jpg")]
print(images)

for image in images:
    path_image = path_name + "/" + image
    coord = coord_calculator(path_image)
    if coord is not None:
        print(image)
        marker_maker(my_map, coord, path_image, image)

my_map.save("my_map.html")

chrome_path = "c:/Program Files/Google/Chrome/Application/chrome.exe %s"

webbrowser.get(chrome_path).open("file:///c%3A/Users/mariu/OneDrive/Desktop/Code/PlacePicture/my_map.html")
