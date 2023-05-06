from pyautogui import *
from time import sleep

with open("config.yml","r") as config:
    filename=config.readline()

with open(filename,"r") as targetfile:
    for cmd in targetfile:
        if "write" in cmd:
            command = cmd.split()
            texttowrite = " ".join([part for part in command if part != "write"])
            write(texttowrite)
        if "delay" in cmd:
            command = cmd.split()
            delay = " ".join([part for part in command if part != "delay"])
            delay = float(delay)
            sleep(delay)
        if "press" in cmd:
            command = cmd.split()
            key = " ".join([part for part in command if part != "press"])
            press(key)
        if "enter" in cmd:
            press("enter")
        elif "GUI" in cmd:
            press("winleft")