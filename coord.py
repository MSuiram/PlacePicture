from PIL import Image
import PIL.ExifTags

def coord_calculator(path : str):
    image = Image.open(path)

    exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in image._getexif().items()
    if k in PIL.ExifTags.TAGS
    }

    if "GPSInfo" in exif:
        if 2 in exif['GPSInfo'] and 4 in exif['GPSInfo']:
            north = exif['GPSInfo'][2]
            east = exif['GPSInfo'][4]

            lat = ((((north[0]*60) + north[1])*60) + north[2]) / 60 / 60
            lng = ((((east[0]*60) + east[1])*60) + east[2]) / 60 / 60

            lat, lng = float(lat), float(lng)
            return [lat, lng]
        else:
            return None
    else:
        return None