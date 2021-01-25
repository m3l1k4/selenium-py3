# #https://sites.google.com/a/chromium.org/chromedriver/downloads
# #/usr/local/bin
# import selenium
# # import os

# from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys

# PATH = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(PATH)
# driver.get("https://www.melika.dev/")


import selenium
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://stackoverflow.com/users/login')