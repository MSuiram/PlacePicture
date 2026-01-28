import folium
import os
import webbrowser
from marker_maker import marker_maker
from coord import coord_calculator

def creat_folium(map_name, paths: str):
    my_map = folium.Map()
    paths = paths.split("\\")
    path_pictures = '/'.join(paths)

    images = [img for img in os.listdir(path_pictures) if img.endswith(".jpg")]
    print(images)

    for image in images:
        path_image = path_pictures + "/" + image
        print(path_image)
        coord = coord_calculator(path_image)
        if coord is not None:
            print(image)
            marker_maker(my_map, coord, path_image, image)

    my_map.save(f"{map_name}.html")

    chrome_path = "c:/Program Files/Google/Chrome/Application/chrome.exe %s"

    webbrowser.get(chrome_path).open(f"file:///c%3A/Users/mariu/OneDrive/Desktop/Code/PlacePicture/{map_name}.html")
