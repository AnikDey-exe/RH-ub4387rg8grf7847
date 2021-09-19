from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import pandas as pd
import requests

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# browser = webdriver.Chrome(executable_path="C:/Users/manas/Dropbox/My PC (LAPTOP-OEFAVRL0)/Downloads/chromedriver_win32/chromedriver.exe",options=options)
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
# browser.get(url)

pages = requests.get(url, verify=False)
print(pages)

# url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
# browser = webdriver.Chrome('C:/Users/manas/Dropbox/My PC (LAPTOP-OEFAVRL0)/Downloads/chromedriver_win32/chromedriver')
# browser.get(url)

time.sleep(10)

def scrape():
    headers = ["proper_name", "distance", "mass", "radius"]
    planet_data = []

    for i in range(0, 1):
        soup = BeautifulSoup(pages.text, "html.parser")

        stars = soup.find("table")

        for tr_tag in stars.find_all("tr", attrs={"class"}):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            row = [i.text.rstrip() for i in td_tags]
            temp_list.append(row)

            # for index, td_tag in enumerate(td_tags):
            #     if index == 0:
            #         temp_list.append(td_tag.find_all("a")[0].contents[0])
            #         # temp_list.append(td_tag.find_all("span")[0].contents[0])
            #     else:
            #         try:
            #             temp_list.append(td_tag.contents[0])
            #         except:
            #             temp_list.append("")

            #     print(temp_list)

            planet_data.append(temp_list)
            print(temp_list)
            
        print(i)

        # browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("webscrapper_1.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()