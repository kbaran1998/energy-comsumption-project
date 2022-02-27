from re import S
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def current_time():
    return round(time.time())

# higher values mean faster scrolling
scrollspeed = 5;
# total execution time in seconds
totalTime = 30
# recording the starttime of the program
starttime = current_time()

# the page to load
page = "https://en.wikipedia.org/wiki/World_energy_supply_and_consumption"

# Installing the chrome driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Loading an innitial page.
driver.get(page)

# maximizing the window
driver.maximize_window()

# finding the total height
total_height = int(driver.execute_script("return document.body.scrollHeight"))
# scrolling through the page
for j in range(1, total_height, scrollspeed):
  driver.execute_script("window.scrollTo(0, {});".format(j))

# wait until the total time is up.
time.sleep(totalTime-(current_time() - starttime))

driver.quit()


