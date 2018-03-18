from selenium import webdriver
import os
import requests
import time
import subprocess

driver = webdriver.Chrome()

def get_page(pageNumber):
    url = 'https://www.congress.gov/members?q=%7B%22congress%22%3A%22115%22%7D&pageSize=250&page='
    url = url + str(pageNumber)
    driver.get(url)

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

    # last image for pageSize=250 is //*[@id="main"]/ol/li[499]/div[2]/div[1]/img 
    for num in range(0, 500):
        try:
            link_url = driver.find_element_by_xpath('//*[@id=\"main\"]/ol/li[%d]/div[2]/div[1]/img' % num)
        except:
            continue
        image = link_url.get_attribute('src')

        name = link_url.get_attribute('alt')
        lastName = name.split(",")[0]
        firstName = name.split(",")[1]
        new_filename = lastName + firstName + '.jpg'

        print(image)
        filename = download_file(image, new_filename)
        subprocess.call(['convert', filename, '-colorspace', 'Gray', filename])

for i in range(1,4):
    some_data = get_page(i)
    time.sleep(1)

driver.close()
