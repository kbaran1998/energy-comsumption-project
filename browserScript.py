
# Importing selenium and the webdrivers.
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Installing the chrome driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Loading a page.
driver.get("https://en.wikipedia.org/wiki/World_energy_supply_and_consumption")

# maximizing the window
driver.maximize_window()

# printing the title of the page.
print(driver.title)

time.sleep(1)

# interacting with the page.

# Smoothly Scrolling down the entire page.
total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
driver.close()