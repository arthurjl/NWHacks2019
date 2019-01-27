#! python3
# InstagramDataScraping.py
# Scrapes through Instagram to collect posts and post data

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

# Find username field
usernameField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

# Find password field
passwordField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

usernameField.send_keys('eatsbyjake')
passwordField.send_keys('ryantruemvp')

# Find login button
loginButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Log in"]')))
loginButton.click()

# grab by css selector
# article > image

srcList = []
time.sleep(5)
pictures = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article > div img")))
for picture in pictures:
	srcList.append(picture.get_attribute("src"))

nameList = []
names = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article header h2 > a")))
for name in names:
	nameList.append(name.get_attribute("title"))

likesList = []
hearts = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article div section div a > span")))
for heart in hearts:
	likedList.append(heart)

print(srcList)
print(len(srcList))
print(nameList)
print(len(nameList))
print(likedList)
print(len(likedList))