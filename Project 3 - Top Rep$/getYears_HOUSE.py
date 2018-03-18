from selenium import webdriver
import os
import csv
import time

driver = webdriver.Chrome()

def get_page(pageNumber):
    url = 'https://www.congress.gov/members?q=%7B%22congress%22%3A%22115%22%7D&pageSize=250&page='
    url = url + str(pageNumber)
    driver.get(url)

    output = []

    for num in range(0, 500):
        try:
            repName = driver.find_element_by_xpath('//*[@id="main"]/ol/li[%d]/span/a' % num).text
            yearsInService = driver.find_element_by_xpath('//*[@id="main"]/ol/li[%d]/div[2]/div[2]/span[4]/span/ul/li' % num).text
        except:
            continue

        item = (repName, yearsInService)

        output.append(item)

    return output

all_data = []

for i in range(1,4):
    some_data = get_page(i)
    all_data = all_data + some_data
    time.sleep(1)

print(all_data)

myFile = open('years_house_better.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(all_data)

driver.close()
