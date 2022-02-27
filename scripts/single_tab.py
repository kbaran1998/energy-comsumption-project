"""Importing selenium and the webdrivers."""
import os
import configparser
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

SCROLL_SPEED = 5

config = configparser.ConfigParser()
config.read('configurations.ini')

# Installing the chrome driver.
driver = webdriver.Chrome(executable_path=config['DRIVER_PATHS']['CHROME_EXE_PATH'])
# Loading an initial page.
driver.get("https://google.com")

# maximizing the window
driver.maximize_window()

# finding the total height
total_height = int(driver.execute_script("return document.body.scrollHeight"))

# scrolling through the page
for j in range(1, total_height, SCROLL_SPEED):
    driver.execute_script(f"window.scrollTo(0, {j});")
# closing the page
driver.close()

driver.quit()
