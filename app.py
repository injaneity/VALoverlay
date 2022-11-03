#pip installs:
#numpy
#pillow
#pyautogui (related to pillow)
#pywin32

import cv2 as cv
import numpy as np
import os
import win32gui

from time import time
from wincap import ValCapture
from threading import Timer

hwnd_input = 0x30124c

# initialize the WindowCapture class
wincap = ValCapture(hwnd_input)#('Spotify Premium')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    cv.namedWindow('Computer Vision', cv.WND_PROP_FULLSCREEN)
    cv.setWindowProperty('Computer Vision', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow('Computer Vision', screenshot)
    cv.moveWindow('Computer Vision', 1905, 300)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')