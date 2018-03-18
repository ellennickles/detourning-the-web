from selenium import webdriver
import os
import csv
import time

driver = webdriver.Chrome()

def get_page(pageNumber):
    url = 'https://www.congress.gov/members?pageSize=100&q=%7B%22congress%22%3A%22115%22%2C%22chamber%22%3A%22Senate%22%7D&page='
    url = url + str(pageNumber)
    driver.get(url)

    output = []

    for num in range(0, 200):
        try:
            repName = driver.find_element_by_xpath('//*[@id=\"main\"]/ol/li[%d]/div[2]/div[1]/img' % num).get_attribute('alt')
            yearsInService = driver.find_element_by_xpath('//*[@id="main"]/ol/li[%d]/div[2]/div[2]/span[3]/span/ul/li' % num).text
        except:
            continue

        item = (repName, yearsInService)

        output.append(item)

    return output

all_data = []

for i in range(1,3):
    some_data = get_page(i)
    all_data = all_data + some_data
    time.sleep(1)

print(all_data)

myFile = open('senate.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(all_data)

driver.close()
