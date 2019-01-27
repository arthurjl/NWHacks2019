#! python3
# InstagramDataScraping.py
# Scrapes through Instagram to collect posts and post data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/?hl=en')