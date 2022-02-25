
# Importing selenium and the webdrivers.
import time
from selenium import webdriver
import selenium.webdriver.support.ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

scrollspeed = 5;

# list of 10 random wiki pages.
pages = ["https://en.wikipedia.org/wiki/World_energy_supply_and_consumption"
        , "https://en.wikipedia.org/wiki/Richard_Lane_(rugby_union)"
        , "https://en.wikipedia.org/wiki/Solid_State_Ionics"
        , "https://en.wikipedia.org/wiki/The_Scoundrel_(1935_film)"
        , "https://en.wikipedia.org/wiki/Knut_Anders_S%C3%B8rum"
        , "https://en.wikipedia.org/wiki/Finn_Schiander"
        , "https://en.wikipedia.org/wiki/Loren_P._Woods"
        , "https://en.wikipedia.org/wiki/Comparison_of_neurofeedback_software"
        , "https://en.wikipedia.org/wiki/Lombardo_Ontiveros"
        , "https://en.wikipedia.org/wiki/Holy_Cross_Church,_Rectory_and_School"]

# Installing the chrome driver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Loading an innitial page.
driver.get("https://google.com")

# maximizing the window
driver.maximize_window()

for i in range(0, 9):
  # opening a new emtpy window
  driver.execute_script("window.open('');")

  # switching to the new window
  driver.switch_to.window(driver.window_handles[1])

  # opening a random wiki page
  driver.get(pages[i])

  # finding the total height
  total_height = int(driver.execute_script("return document.body.scrollHeight"))
  # scrolling through the page
  for j in range(1, total_height, scrollspeed):
    driver.execute_script("window.scrollTo(0, {});".format(j))
  # closing the page
  driver.close()
  driver.switch_to.window(driver.window_handles[0])

driver.quit()