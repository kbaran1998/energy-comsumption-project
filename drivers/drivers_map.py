"""Selenium webdriver meta module."""
from selenium import webdriver
from webdriver_manager.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

VALID_DRIVER_NAMES = {"chrome", "firefox", "ie", "edge", "opera"}

def get_chrome() :
    """Function that downloads Chrome Selenium webdriver."""
    return webdriver.Chrome(
        service=webdriver.chrome.service.Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        )
    )

def get_firefox() :
    """Function that downloads Firefox Selenium webdriver."""
    return webdriver.Firefox(
        service=webdriver.firefox.service.Service(
            GeckoDriverManager().install()
        )
    )

def get_ie() :
    """Function that downloads Internet Explorer Selenium webdriver."""
    return webdriver.Ie(
        service=webdriver.ie.service.Service(
            IEDriverManager().install()
        )
    )

def get_edge() :
    """Function that downloads Edge Selenium webdriver."""
    return webdriver.Edge(
        service=webdriver.edge.service.Service(
            EdgeChromiumDriverManager().install()
        )
    )

def get_opera() :
    """Function that downloads Opera Selenium webdriver."""
    return webdriver.Opera(
        executable_path=OperaDriverManager().install()
    )


DRIVERS_DICT = {
    "chrome" : get_chrome,
    "firefox" : get_firefox,
    "ie" : get_ie,
    "edge" : get_edge,
    "opera" : get_opera,
}
