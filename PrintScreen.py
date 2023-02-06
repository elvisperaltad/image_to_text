import pyautogui
import time
from imgToText import *

print("Start Print Screen")
time.sleep(2)
myScreenshot = pyautogui.screenshot(region=(100,180, 300, 400))
myScreenshot.save(r'C:\Users\pc\Desktop\Test\images\p3.png')
print("End")

main()