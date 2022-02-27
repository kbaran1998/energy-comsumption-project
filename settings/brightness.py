"""Module for setting brightness of the screen."""
import screen_brightness_control as sbc


def set_screen_brightness(percentage):
    """Sets the screen brightness (forces it into percentage)"""
    try:
        sbc.set_brightness(max(0, min(100, percentage)))
    except sbc.ScreenBrightnessError as error:
        print(error)
