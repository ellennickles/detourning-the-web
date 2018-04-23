# adapted from: https://github.com/LevPasha/Instagram-API-python
import json
from InstagramAPI import InstagramAPI
import get_images
import time
import random

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

InstagramAPI = InstagramAPI(creds["login"], creds["password"])
InstagramAPI.login()

# for i in range(0,2457):
for i in range(0,1):
    data = get_images.get_Satellite_Image(i)

    path = data[0]
    landfill_name = data[1]
    state = data[2]
    latitude_caption = data[3]
    longitude_caption = data[4]
    status = data[5]
    tons = data[6]

    caption = 'in #' + state + '\n\n' + landfill_name + '\nLat Lon: ' + latitude_caption + ' ' + longitude_caption + '\nStatus: ' + status + '\nWaste in Place (tons): ' + tons + '\n\n#Earth #Landfill #Landscape #Lifestyle #Photograph #Photooftheday'

    InstagramAPI.uploadPhoto(path, caption=caption)
    n = random.randint(180, 600)
    print n
    time.sleep(n)
