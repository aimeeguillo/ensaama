from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_gps_coordinates(chemin_image):
    image = Image.open("photo.jpg")
    exif_data = image._getexif()

    gps_info = {}
    for tag_id, valeur in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "GPSInfo":
            for gps_tag_id, gps_valeur in valeur.items():
                gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                gps_info[gps_tag] = gps_valeur

    def convertir_en_degres(valeur):
        d, m, s = valeur
        return d + (m / 60.0) + (s / 3600.0)

    lat = convertir_en_degres(gps_info["GPSLatitude"])
    if gps_info["GPSLatitudeRef"] != "N":
        lat = -lat

    lon = convertir_en_degres(gps_info["GPSLongitude"])
    if gps_info["GPSLongitudeRef"] != "E":
        lon = -lon
    return lat, lon

coordonnees = get_gps_coordinates("photo.jpg")

if coordonnees:
    lat, lon = coordonnees
    print(f"Latitude : {lat}, Longitude : {lon}")
    print(f"Google Maps : https://www.google.com/maps?q={lat},{lon}")
