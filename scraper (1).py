from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/TRUSTANA MARKETING/Downloads/chromedriver_win32.zip")
browser.get(START_URL)

time.sleep(20)
def scrape():
    headers=["Name","Distance","Mass","Radius"]
    planet_data=[]
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for i in 1:                                                            
        for th_tag in soup.find_all("th",attrs={"class","wikitable sortable jquery-tablesorter"}):
            tr_tags= tr_tag.find_all("tr")
            temp_list=[]
            for index,tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
    with open("scrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)


scrape()


    