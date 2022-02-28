from re import S
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import argparse

parser = argparse.ArgumentParser(description='Power usage test tool.')

parser.add_argument('--p', '-page', type=str, help='the webpage to open and scrollthrough',
                    default='')
parser.add_argument('--s', '-seconds', type=int, help='total duration',
                    default=5)

args = vars(parser.parse_args())

# parsing the page to load
page = args.get('p')
print(page)
if(page == "") :
  print("cannot load empty page!")
  exit()

def current_time():
    return round(time.time())

# total execution time in seconds
totalTime = args.get('s')

# higher values mean faster scrolling
scrollspeed = 5;

# recording the starttime of the program
starttime = current_time()



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


