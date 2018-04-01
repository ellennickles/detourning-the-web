import requests
import os
import json
import time
import random

def download_file(url, local_filename=None):
    # from: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    if local_filename is None:
        local_filename =  url.split('/')[-1]

    if os.path.exists(local_filename):
        return local_filename

    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename

def get_images(num):
    url = 'https://duckduckgo.com/i.js?q=vintage%20urinals&o=json&p=-1&s=' + str(num) + '&u=yahoo&f=,,,&l=us-en'

    response = requests.get(url).json()

    for image in response['results']:
        image = image['image']

        if image not in output:
            output.append(image)
        # print image

output = []

for i in range(50, 301, 50):
    get_images(i)
    time.sleep(2)

random_image = (random.choice(output))
savedname = 'pic.jpg'
download_file(random_image, savedname)
