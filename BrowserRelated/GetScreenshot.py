import os
from sre_constants import SUCCESS
import sys
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

FILENAME = "screen.png"
brave_path = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
#proxy = 'cproxy.okinawa-ct.ac.jp:8080'

options = webdriver.ChromeOptions()
options.binary_location = brave_path
options.add_argument('--hide-scrollbars')
options.add_argument('--headless')
#options.add_argument('--proxy-server=http://%s' % proxy)
options.add_argument('--no-sandbox')
options.add_argument('start-maximized')
options.add_argument('enable-automation')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument("--remote-debugging-port=9222")
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
driver = webdriver.Chrome('C:\\Users\\mi181350\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\chromedriver_binary\\chromedriver',options=options)

num_success, num_error = 0,0
all = 0

os.system('cls')
with open("url.csv", 'r') as f:
    csv.reader(f)
    for url in csv.reader(f):
        all = all + 1
        print("%s" %all)
        driver.get( url[0] )
        sleep(6)
        h = driver.execute_script("return document.body.scrollHeight;")
        driver.set_window_size(1300,h)
        hh = driver.execute_script("return document.body.scrollHeight;")
        name = "Image\\%s.png" % driver.title

        if (driver.save_screenshot(name) is True ):
            print("success\n")
            num_success = num_success + 1

        else:
            print("error\n")
            num_error = num_error + 1
driver.quit()
print("Success:%d  Error:%d  All:%d" %(num_success, num_error, all) )

"""
Reference
- [【Python】seleniumでWeb ページ全体のスクリーンショットを撮れない場合の解決方法](https://tsukimitech.com/python-selenium-web/#toc4)
- [PowerShell script to operate Brave with Chrome Driver](https://www.ka-net.org/blog/?p=14740)
"""