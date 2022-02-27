import screen_brightness_control as sbc
try:
    sbc.set_brightness(0)
except sbc.ScreenBrightnessError as error:
    print(error)
