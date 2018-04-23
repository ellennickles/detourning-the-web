# adapted from: https://github.com/joshbegley/prisonmap/blob/master/processing-sketch.txt
# data sourced from Google Maps and the Landfill Methane Outreach Program, a voluntary #EPA program
# see https://www.epa.gov/lmop/landfill-technical-data from Feb 2018
import requests
import shutil
import json
import time
from PIL import Image

with open('creds.json', 'r') as infile:
    creds = json.load(infile)

with open('landfills.json', 'r') as infile:
    data = json.load(infile)

api_key = (creds['api_key'])
zoom = '16'

def get_Satellite_Image(i):
    id = data[i]['My ID']
    landfill_name = data[i]['Landfill Name']
    latitude = str(data[i]['Latitude'])
    longitude = str(data[i]['Longitude'])

    state = data[i]['State Full Insta']
    latitude_caption = str(data[i]['Latitude Caption'])
    longitude_caption = str(data[i]['Longitude Caption'])
    status = data[i]['Current Landfill Status']
    tons = data[i]['Waste in Place (tons)']

    url = 'http://maps.googleapis.com/maps/api/staticmap?center=' + latitude + ',' + longitude + '&zoom=' + zoom + '&scale=2&size=640x640&maptype=satellite&sensor=false&key=' + api_key + '&junk=.jpg'

    # from: https://stackoverflow.com/questions/13137817/how-to-download-image-using-requests?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            path = 'images/img' + str(id) + '.jpg'
            with open(path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print(e)

    newFile = Image.new('RGB', (1080,1080), (0,0,0))
    downloadedImage = Image.open(path)
    downloadedImage = downloadedImage.resize((1080,1080))
    newFile.paste(downloadedImage, (0,0))
    newFile.save(path)

    return path, landfill_name, state, latitude_caption, longitude_caption, status, tons
