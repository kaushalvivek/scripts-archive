import time
import smtplib
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# WEB DRIVER
# -----------------
options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.get("https://www.ces.tech/Conference/Speaker-Directory")

articles = browser.find_element_by_id('speaker-listing')
# print(articles)
SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
