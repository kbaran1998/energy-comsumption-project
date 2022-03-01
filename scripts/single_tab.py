"""
A single tab scroll test case.
"""
import os
import sys
import time
import argparse
import configparser
from selenium import webdriver

# gets the current time in seconds.
def current_time():
    """Gets the current time in seconds (rounded)"""
    return round(time.time())

# recording the starttime of the program
starttime = current_time()

# setting up the parser
parser = argparse.ArgumentParser(description='Power usage test tool.')

parser.add_argument('--p', '-page', type=str, help='the webpage to open and scrollthrough',
                    default='')
parser.add_argument('--s', '-seconds', type=int, help='total duration',
                    default=5)

args = vars(parser.parse_args())

# parsing the page to load
page = args.get('p')
print(f"INFO: Page loaded - {page}")

if page == "" :
    print("ERROR: cannot load empty page!")
    sys.exit()

# total execution time in seconds
totalTime = args.get('s')

# higher values mean faster scrolling
SCROLL_SPEED = 5

config = configparser.ConfigParser()
config.read('configurations.ini')

# Installing the chrome driver.
driver = webdriver.Chrome(executable_path=config['DRIVER_PATHS']['CHROME_EXE_PATH'])

# Loading an initial page.
driver.get(page)

# maximizing the window
driver.maximize_window()

# finding the total height
total_height = int(driver.execute_script("return document.body.scrollHeight"))
# scrolling through the page
for j in range(1, total_height, SCROLL_SPEED):
    driver.execute_script(f"window.scrollTo(0, {j});")

# wait until the total time is up.
SLEEP_TIME = totalTime - (current_time() - starttime)

if SLEEP_TIME > 0:
    time.sleep(SLEEP_TIME)

driver.quit()
