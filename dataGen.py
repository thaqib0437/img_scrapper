from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import time
import sys
import os
import math

def get_imgs(download, n):
    #taking user input
    print("What do you want to download?")
    site = 'https://www.google.com/search?tbm=isch&q='+download
    NUM_INPUTS = int(n)
    #providing driver path
    driver = webdriver.Firefox(executable_path = 'C:\driver\geckodriver.exe')

    #passing site url
    driver.get(site)


    #if you just want to download 10-15 images then skip the while loop and just write
    #driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


    #below while loop scrolls the webpage 7 times(if available)

    i = 0
    scrolls = 0 if NUM_INPUTS <= 10 else math.ceil(NUM_INPUTS*0.1)
    while i<scrolls:  
        #for scrolling page
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        
        try:
            #for clicking show more results button
            driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
        except Exception as e:
            pass
        time.sleep(5)
        i+=1

    #parsing
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    #closing web browser
    driver.close()


    #scraping image urls with the help of image tag and class used for images
    img_tags = soup.find_all("img", class_="rg_i")


    count = 0
    cwd = os.getcwd()
    os.mkdir(cwd + '/' + download)
    for j,i in enumerate(img_tags):
        #print(i['src'])
        try:
            #passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], str(cwd)+ '/' + download +'/'+ str(count)+".jpg")
            count+=1
            print("Number of images downloaded = "+str(count),end='\r')
        except Exception as e:
            pass
        if(j >= NUM_INPUTS - 1):
            break



if __name__ == "__main__":
    download = input('What do you want to downlaod')
    n = input("How many images")
    get_imgs(download, n)
    