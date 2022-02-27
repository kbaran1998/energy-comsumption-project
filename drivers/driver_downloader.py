"""Program that gets the driver for a browser."""
# pylint: disable=import-error
from drivers_map import VALID_DRIVER_NAMES, DRIVERS_DICT
from selenium.common.exceptions import WebDriverException


def download_all_web_drivers():
    """Function that downloads all browser drivers."""
    download_selected_web_drivers(VALID_DRIVER_NAMES)

def download_selected_web_drivers(driver_names_list):
    """Function that downloads selected browser drivers."""
    driver_names_set = set(driver_names_list)
    drivers_to_get = VALID_DRIVER_NAMES.intersection(driver_names_set)
    download_drivers_dict = {}
    for driver_name in drivers_to_get:
        try:
            download_drivers_dict[driver_name] = DRIVERS_DICT[driver_name]()
            download_drivers_dict[driver_name].quit()
        except WebDriverException :
            print("Install failed: Already installed or exists")
    return download_drivers_dict

download_all_web_drivers()
