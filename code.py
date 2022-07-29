from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By
url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('C:/Users/yena0/Downloads/chromedriver_win32/chromedriver')
browser.get(url)
time.sleep(10)

def scrapdata():
    headers = ['name','LIGHT_YEARS_FROM_EARTH','PLANET_MASS','STELLAR_MAGNITUDE','DISCOVERY_DATE']
    planetdata = []
    for f in range(0,2):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        allultags = soup.find_all('ul',attrs={'class','exoplanet'})
        for eachul in allultags:
            alllitags = eachul.find_all('li')
            templist = []
            for index,eachli in enumerate(alllitags):
                if(index == 0):
                    templist.append(eachli.find_all('a')[0].contents[0])
                else:
                    templist.append(eachli.contents[0])
            planetdata.append(templist)
        browser.find_element( By.XPATH, '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scraper.csv','w',newline='') as X:
        csvwriter = csv.writer(X)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)
scrapdata()