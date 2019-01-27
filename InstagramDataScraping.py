#! python3
# InstagramDataScraping.py
# Scrapes through Instagram to collect posts and post data

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def get_data():
	browser = webdriver.Firefox()
	browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

	# Find username field
	usernameField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

	# Find password field
	passwordField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

	usernameField.send_keys('LETZy33tTHEWh34t')
	passwordField.send_keys('arthuristhenewjake')

	# Find login button
	loginButton = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Log in"]')))
	loginButton.click()

	# grab by css selector
	# article > image

	srcList, nameList, likedList = [], [], []
	for i in range(1):
		time.sleep(5)
		pictures = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article > div img")))
		for picture in pictures:
			srcList.append(picture.get_attribute("src"))

		names = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article header h2 > a")))
		for name in names:
			nameList.append(name.get_attribute("title"))
	
		hearts = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article div section div a > span")))
		# article > div > section > div > span > span (temp new selector)

		# article div section div a > span (old selector for likes)
		for heart in hearts:
			likedList.append(heart.text)

		while (len(likedList) < len(srcList)):
			likedList.append("n/a")

		htmlElem = browser.find_element_by_tag_name('html')
		htmlElem.send_keys(Keys.END)

	print(len(srcList))
	print(len(nameList))
	print(len(likedList))


	postList = []
	for i in range(len(srcList)):
		thisdict =	{
			"src": srcList[i],
			"poster": nameList[i],
			"likes": likedList[i]
		}
		postList.append(thisdict)

	return postList





# for element in self.driver.find_elements_by_tag_name('img'):
#        print element.text
#        print element.tag_name
#        print element.parent
#        print element.location
#        print element.size